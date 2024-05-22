#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) (2017-2023) Chatopera Inc.<https://www.chatopera.com>, All Rights Reserved
#
#
# File: /Users/hain/ai/insuranceqa-corpus-zh/pypi/insuranceqa_data/__init__.py
# Author: Chatopera Inc.<https://www.chatopera.com>
# Date: 2017-07-28:10:47:28
# Modified by Xuming Lin in 2018-01-23 23:50
#
#===============================================================================
from __future__ import print_function

__copyright__ = "Copyright (c) Chatopera Inc.<https://www.chatopera.com> 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-28:10:47:28"

import os
import sys
import gzip
import json
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir)


import shutil
from chatoperastore import download_licensedfile, extract_licensedfile

INSQA_DL_LICENSE = os.environ.get("INSQA_DL_LICENSE", None)
DOWNLOAD_FOLDER_PATH = os.path.join(curdir, "data")
DOWNLOADED_FILEPATH = os.path.join(DOWNLOAD_FOLDER_PATH, "corpus.tar.gz")
CORPUS_FOLDER_PATH = os.path.join(DOWNLOAD_FOLDER_PATH, "corpus")


'''
Sponsorship
'''
print("\n insuranceqa_data, Project home: %s" % ("https://github.com/chatopera/insuranceqa-corpus-zh"))
print("\n Project Sponsored by Chatopera")
print("\n  deliver your chatbots with Chatopera Cloud Services --> https://bot.chatopera.com\n")
print("\n Module file path: %s" % __file__)
print("\n ************ NOTICE ************")
print("  Require license to download file(s) package, purchase from https://store.chatopera.com/product/insqa001")
print(" ********************************\n")


def download_corpus(force=False):
    '''
    Download and extract file
    '''
    if not os.path.exists(DOWNLOAD_FOLDER_PATH):
        os.mkdir(DOWNLOAD_FOLDER_PATH)

    if force:
        if os.path.exists(CORPUS_FOLDER_PATH): shutil.rmtree(CORPUS_FOLDER_PATH, ignore_errors=True)
        if os.path.exists(DOWNLOADED_FILEPATH): shutil.rmtree(DOWNLOADED_FILEPATH, ignore_errors=True)
        
    if not os.path.exists(DOWNLOADED_FILEPATH):
        if not INSQA_DL_LICENSE:
            print("[insuranceqa_data] first, get your license id and export it as ENV INSQA_DL_LICENSE, e.g. `export INSQA_DL_LICENSE=FOOBAR`")
            raise ValueError("Require license to download file(s) package, purchase from https://store.chatopera.com/product/insqa001");

        print("[insuranceqa_data] download only happens the corpus is not present, mostly by first time run `import insuranceqa_data` after installation.")
        download_licensedfile(INSQA_DL_LICENSE, DOWNLOADED_FILEPATH)
        extract_licensedfile(DOWNLOADED_FILEPATH, DOWNLOAD_FOLDER_PATH)

        if not os.path.exists(CORPUS_FOLDER_PATH):
            print("[insuranceqa_data] download_corpus error")
            raise FileNotFoundError("Dir %s not found" % CORPUS_FOLDER_PATH)


def load(data_path, download = False):
    if (not os.path.exists(data_path)) and download:
        download_corpus(force=True)
    elif not os.path.exists(data_path):
        raise AssertionError("Data path not found %s" % data_path)

    with gzip.open(data_path, 'rb') as f:
        data = json.loads(f.read())
        return data

'''
pool data are translated Chinese data with Google API from original English data
'''

def load_pool_test(data_path=None):
    download = False
    if data_path is None:
        POOL_TEST_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pool', 'test.json.gz')
        download = True
    else:
        POOL_TEST_DATA = os.path.join(data_path, 'pool', 'test.json.gz')
    return load(POOL_TEST_DATA, download=download)

def load_pool_valid(data_path=None):
    download = False
    if data_path is None:
        POOL_VALID_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pool', 'valid.json.gz')
        download = True
    else:
        POOL_VALID_DATA = os.path.join(data_path, 'pool', 'valid.json.gz')
    return load(POOL_VALID_DATA, download=download)

def load_pool_train(data_path=None):
    download = False
    if data_path is None:
        POOL_TRAIN_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pool', 'train.json.gz')
        download = True
    else:
        POOL_TRAIN_DATA = os.path.join(data_path, 'pool', 'train.json.gz')
    return load(POOL_TRAIN_DATA, download=download)

def load_pool_answers(data_path=None):
    download = False
    if data_path is None:
        POOL_ANS_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pool', 'answers.json.gz')
        download = True
    else:
        POOL_ANS_DATA = os.path.join(data_path, 'pool', 'answers.json.gz')
    return load(POOL_ANS_DATA, download=download)

# def __test_qa():
#     d = load_train()
#     for x in d:
#         print('index %s value: %s ++$++ %s ++$++ %s %s' % (x, d[x]['zh'], d[x]['en'], d[x]['answers'], d[x]['negatives']))

# def __test_answers():
#     d = load_answers()
#     for x in d:
#         print('index %s: %s ++$++ %s' % (x, d[x]['zh'], d[x]['en']))

'''
pair data are segmented and labeled after pool data
'''

def load_pairs_vocab(data_path=None):
    '''
    Load vocabulary data
    '''
    download = False
    if data_path is None:
        PAIR_VOCAB_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pairs', 'iqa.vocab.json.gz')
        download = True
    else:
        PAIR_VOCAB_DATA = os.path.join(data_path, 'pairs', 'iqa.vocab.json.gz')
    return load(PAIR_VOCAB_DATA, download=download)

def load_pairs_test(data_path=None):
    download = False
    if data_path is None:
        PAIR_TEST_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pairs','iqa.test.json.gz')
        download = True
    else:
        PAIR_TEST_DATA = os.path.join(data_path, 'pairs','iqa.test.json.gz')
    return load(PAIR_TEST_DATA, download=download)

def load_pairs_valid(data_path=None):
    download = False 
    if data_path is None:
        PAIR_VALID_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pairs','iqa.valid.json.gz')
        download = True
    else:
        PAIR_VALID_DATA = os.path.join(data_path, 'pairs','iqa.valid.json.gz')
    return load(PAIR_VALID_DATA, download=download)

def load_pairs_train(data_path=None):
    download = False 
    if data_path is None:
        PAIR_TRAIN_DATA = os.path.join(CORPUS_FOLDER_PATH, 'pairs','iqa.train.json.gz')
        download = True
    else:
        PAIR_TRAIN_DATA = os.path.join(data_path, 'pairs','iqa.train.json.gz')
    return load(PAIR_TRAIN_DATA, download=download)

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
