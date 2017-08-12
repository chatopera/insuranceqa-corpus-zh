#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/InsuranceQA-Machine-Learning/deep_qa_1/visual.py
# Author: Hai Liang Wang
# Date: 2017-08-09:21:56:58
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-08-09:21:56:58"

import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(curdir))

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import csv
import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# style.use('fivethirtyeight')
style.use(["ggplot", os.path.join(curdir, "tensorflowvisu.mplstyle")])
fig = plt.figure()
ax = fig.add_subplot(111)

graph_data_f = os.path.join(curdir, '..', 'tmp', 'loss.txt')

def init():
    with open(graph_data_f, "w") as f:
        f.write('')

def plot(step, loss):
    with open(graph_data_f, "a") as f:
        f.write('%s\t%s\n' % (step, loss))

def animate(i):
    graph_data = np.loadtxt(graph_data_f, skiprows=0, delimiter='\t', unpack=True).transpose()
    steps = graph_data[:,0]
    loss = graph_data[:,1]
    filtered = lowess(loss, steps, is_sorted=True, frac=148.0/len(steps), it=0)
    ax.clear()
    ax.set_xlabel('steps')
    ax.set_ylabel('loss')
    ax.plot(steps, loss, 'r')
    ax.plot(filtered[:,0], filtered[:,1], 'b')

def test_draw():
    ani = animation.FuncAnimation(fig, animate, interval=3000)
    plt.show()

if __name__ == '__main__':
    test_draw()
