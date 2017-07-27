#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: /Users/hain/ai/insuranceqa-corpus/filize.py
# Author: Hai Liang Wang
# Date: 2017-07-26:21:12:34
#
#===============================================================================

"""
   pipe json to file for human review
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-26:21:12:34"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

files = [os.path.join(curdir, 'corpus', 'test.json'), 
    os.path.join(curdir, 'corpus', 'valid.json'), 
    os.path.join(curdir, 'corpus', 'train.json')
]

answers_json = os.path.join(curdir, 'corpus', 'answers.json')

import json

def process(file_path, data):
    with open(file_path + '.txt', 'w') as f:
        for x in data.keys():
            index = x
            info = data[x]
            f.write("%s ++$++ %s ++$++ %s ++$++ %s\n" % (x,  info['domain'], info['zh'], info['en']))

def read_files_qna():
    for x in files:
        with open(x, 'r') as f:
            data = json.load(f)
            process(x, data)

def read_answers():
    with open(answers_json, 'r') as f, open(os.path.join(curdir, 'corpus', 'answers.txt'), 'w') as fout:
        data = json.load(f)
        for x in data.keys():
            index = x
            info = data[x]
            fout.write("%s ++$++ %s ++$++ %s\n" % (index, info['zh'], info['en']))            

def main():
    # read_files_qna()
    read_answers()

if __name__ == '__main__':
    main()
