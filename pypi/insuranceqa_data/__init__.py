#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 Hai Liang Wang, All Rights Reserved
#
#
# File: /Users/hain/ai/insuranceqa-corpus-zh/pypi/insuranceqa_data/__init__.py
# Author: Hai Liang Wang
# Date: 2017-07-28:10:47:28
#
#===============================================================================
from __future__ import print_function

__copyright__ = "Copyright (c) Hai Liang Wang 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-28:10:47:28"

import os
import sys
import gzip
import json
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir)

import wget

def load(data_path):
    if not os.path.exists(data_path):
        # download all pair data
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.test.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.test.json.gz", out = os.path.join(curdir, 'pairs'))
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.train.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.train.json.gz", out = os.path.join(curdir, 'pairs'))
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.valid.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.valid.json.gz", out = os.path.join(curdir, 'pairs'))
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.vocab.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/raw/release/corpus/pairs/iqa.vocab.json.gz", out = os.path.join(curdir, 'pairs'))

        # download all pool data
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/answers.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/answers.json.gz", out = os.path.join(curdir, 'pool'))
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/test.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/test.json.gz", out = os.path.join(curdir, 'pairs'))
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/train.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/train.json.gz", out = os.path.join(curdir, 'pairs'))
        print("\n [insuranceqa_data] downloading data %s ... \n" % "https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/valid.json.gz")
        wget.download("https://github.com/Samurais/insuranceqa-corpus-zh/blob/release/corpus/pool/valid.json.gz", out = os.path.join(curdir, 'pairs'))
        
    with gzip.open(data_path, 'rb') as f:
        data = json.loads(f.read())
        return data

'''
pool data are translated Chinese data with Google API from original English data
'''
POOL_TEST_DATA = os.path.join(curdir, 'pool', 'test.json.gz')
POOL_TRAIN_DATA = os.path.join(curdir, 'pool', 'train.json.gz')
POOL_VALID_DATA = os.path.join(curdir, 'pool', 'valid.json.gz')
POOL_ANS_DATA = os.path.join(curdir, 'pool', 'answers.json.gz')

def load_pool_test():
    return load(POOL_TEST_DATA)

def load_pool_valid():
    return load(POOL_VALID_DATA)

def load_pool_train():
    return load(POOL_TRAIN_DATA)

def load_pool_answers():
    return load(POOL_ANS_DATA)

def __test_qa():
    d = load_train()
    for x in d:
        print('index %s value: %s ++$++ %s ++$++ %s %s' % (x, d[x]['zh'], d[x]['en'], d[x]['answers'], d[x]['negatives']))

def __test_answers():
    d = load_answers()
    for x in d:
        print('index %s: %s ++$++ %s' % (x, d[x]['zh'], d[x]['en']))

'''
pair data are segmented and labeled after pool data
'''
PAIR_TEST_DATA = os.path.join(curdir, 'pairs','iqa.test.json.gz')
PAIR_VALID_DATA = os.path.join(curdir, 'pairs','iqa.valid.json.gz')
PAIR_TRAIN_DATA = os.path.join(curdir, 'pairs','iqa.train.json.gz')
PAIR_VOCAB_DATA = os.path.join(curdir, 'pairs', 'iqa.vocab.json.gz')

def load_pairs_vocab():
    '''
    Load vocabulary data
    '''
    return load(PAIR_VOCAB_DATA)

def load_pairs_test():
    return load(PAIR_TEST_DATA)

def load_pairs_valid():
    return load(PAIR_VALID_DATA)

def load_pairs_train():
    return load(PAIR_TRAIN_DATA)

def __test_pair_test():
    d = load_pairs_test()
    for x in d:
        print("index %s question %s utterance %s label %s" % (x['qid'], x['question'], x['utterance'], x['label']))
        break

if __name__ == '__main__':
    # __test_qa()
    # __test_answers()
    __test_pair_test()
    pass
