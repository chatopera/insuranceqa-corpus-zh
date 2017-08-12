#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2012-2015 Michael Nielsen
# Copyright (c) 2017 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved
#
#
# File: /Users/hain/ai/InsuranceQA-Machine-Learning/deep_qa_1/network.py
# Author: Hai Liang Wang
# Date: 2017-08-08:18:32:05
#
#===============================================================================

"""
   A Simple Network to learning QA.
   
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 Hai Liang Wang. All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-08-08:18:32:05"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(curdir))

import numpy as np
import deep_qa_1.data as corpus
import visual.loss as visual_loss
import visual.accuracy as visual_acc

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

class NeuralNetwork():
    def __init__(self, hidden_layers = [100, 50], 
                 question_max_length = 20, 
                 utterance_max_length = 99, 
                 lr = 0.001, epoch = 10, 
                 batch_size = 100,
                 eval_every_N_steps = 500):
        '''
        Neural Network to train question and answering model
        '''
        self.input_layer_size = question_max_length + utterance_max_length + 1 # 1 is for <GO>
        self.output_layer_size = 2 # just the same shape as labels
        self.layers = [self.input_layer_size] + hidden_layers + [self.output_layer_size] # [2] is for output layer
        self.layers_num = len(self.layers)
        self.weights = [np.random.randn(y, x) for x,y in zip(self.layers[:-1], self.layers[1:])]
        self.biases = [np.random.randn(x, 1) for x in self.layers[1:]]
        self.epoch = epoch
        self.lr = lr
        self.batch_size = batch_size
        self.eval_every_N_steps = eval_every_N_steps
        self.test_data = corpus.load_test()

    def back_propagation(self, x, y_):
        '''
        back propagation algorithm to compute the error rates for every W and b
        '''
        cost = 0.0
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        zs = [] # z vectors
        activations = [x]
        activation = x
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        cost += self.loss_fn(activations[-1], y_)

        # backward
        delta = self.loss_fn_derivative(activations[-1], y_) * sigmoid_derivative(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.layers_num):
            z = zs[-l]
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sigmoid_derivative(zs[-l])
            nabla_b[-l] = delta
            nabla_w[-l] =  np.dot(delta, activations[-l-1].transpose())

        return (nabla_b, nabla_w, cost)

    def loss_fn(self, a, y_):
        # cross-entropy cost fn
        return np.sum(np.nan_to_num(-y_*np.log(a) - (1-y_)*np.log(1-a)))

    def loss_fn_derivative(self, a, y_):
        # maximum likelihood estimation
        return (a-y_)

    def run(self, test = False):
        '''
        Train model with mini-batch stochastic gradient descent.
        '''
        total_step = 0
        for n in range(self.epoch):
            for mini_batch in corpus.load_train():
                nabla_b = [np.zeros(b.shape) for b in self.biases]
                nabla_w = [np.zeros(w.shape) for w in self.weights]
                total_cost = 0.0
                for x, y_ in mini_batch:
                    # here scale the input's word ids with 0.001 for x to make sure the Z-vector can pass sigmoid fn
                    delta_nabla_b, delta_nabla_w, cost = self.back_propagation( \
                                np.reshape(x, (self.input_layer_size, 1)) * 0.001, \
                                np.reshape(y_, (self.output_layer_size, 1)))
                    nabla_b = [ nb+mnb for nb, mnb in zip(nabla_b, delta_nabla_b)]
                    nabla_w = [ nw+mnw for nw, mnw in zip(nabla_w, delta_nabla_w)]
                    total_cost += cost
                self.weights = [ w - (self.lr * w_)/len(mini_batch) for w, w_ in zip(self.weights, nabla_w)]
                self.biases = [ b - (self.lr * b_)/len(mini_batch) for b, b_ in zip(self.biases, nabla_b)]
                total_step += 1
                print("Epoch %s, total step %d, cost %f" % (n, total_step, total_cost/len(mini_batch)))
                visual_loss.plot(total_step, total_cost/len(mini_batch))
                if (total_step % self.eval_every_N_steps ) == 0 and test:
                    accuracy = self.evaluate()
                    print("Epoch %s, total step %d, accuracy %s" % (n, total_step, accuracy))
                    visual_acc.plot(total_step, accuracy)

    def feedforward(self, x):
        '''
        Feedforward network
        '''
        activation = x
        for w, b in zip(self.weights, self.biases):
            z = np.dot(w, activation) + b
            activation = sigmoid(z)
        return activation

    def evaluate(self):
        '''
        evaluate model
        '''
        # for (x,y) in self.test_data:
        #     r = self.feedforward(np.reshape(x, (self.input_layer_size, 1)) * 0.001)
            # print("feedforward", r)
            # print("argmax", np.argmax(r))
            # print("y", y)
            # print("*"*20)
        result = [(np.argmax(self.feedforward(np.reshape(x, (self.input_layer_size, 1)) * 0.001)), y) for (x, y) in self.test_data]
        # print(result)
        print("count", sum(int(y[x] == 1) for (x, y) in result))
        return "%.4f" % ( sum(int(y[x] == 1) for (x, y) in result)/ len(self.test_data))

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * ( 1.0 - sigmoid(x))

def test_train():
    visual_loss.init()
    visual_acc.init()
    nn = NeuralNetwork(epoch = 50, lr = 0.0001, eval_every_N_steps = 200)
    nn.run(test = True)

if __name__ == '__main__':
    test_train()
