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

files = [os.path.join(curdir, 'insuranceqa.pool.100', 'test.json'), 
    os.path.join(curdir, 'insuranceqa.pool.100', 'valid.json'), 
    os.path.join(curdir, 'insuranceqa.pool.100', 'train.json')
]

import json

def process(file_path, data):
    with open(file_path + '.txt', 'w') as f:
        for x in data.keys():
            index = x
            info = data[x]
            f.write("%s ++$++ %s ++$++ %s ++$++ %s\n" % (x,  info['domain'], info['zh'], info['en']))

def read_files():
    for x in files:
        with open(x, 'r') as f:
            data = json.load(f)
            process(x, data)


def main():
    read_files()

if __name__ == '__main__':
    main()
