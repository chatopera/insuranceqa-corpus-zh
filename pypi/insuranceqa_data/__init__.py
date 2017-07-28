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
sys.path.append(curdir)

TEST_DATA = os.path.join(curdir, 'test.json.gz')
TRAIN_DATA = os.path.join(curdir, 'train.json.gz')
VALID_DATA = os.path.join(curdir, 'valid.json.gz')
ANS_DATA = os.path.join(curdir, 'answers.json.gz')

def load(data_path):
    with gzip.open(data_path, 'rb') as f:
        data = json.loads(f.read())
        return data

def load_test():
    return load(TEST_DATA)

def load_valid():
    return load(VALID_DATA)

def load_train():
    return load(TRAIN_DATA)

def load_answers():
    return load(ANS_DATA)

def __test_qa():
    d = load_train()
    for x in d:
        print('index %s value: %s ++$++ %s ++$++ %s %s' % (x, d[x]['zh'], d[x]['en'], d[x]['answers'], d[x]['negatives']))

def __test_answers():
    d = load_answers()
    for x in d:
        print('index %s: %s ++$++ %s' % (x, d[x]['zh'], d[x]['en']))

if __name__ == '__main__':
    __test_qa()
    __test_answers()
    pass
