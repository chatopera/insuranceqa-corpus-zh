#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: /Users/hain/tmp/InsuranceQA_temp/read_gz.py
# Author: Hai Liang Wang
# Date: 2017-07-25:12:21:52
#
#===============================================================================

"""
   jsonfiy insuranceqa v2 data
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-25:12:21:52"


from functools import reduce
import os
import sys
import json
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

label2answer="data/V2/InsuranceQA.label2answer.raw.encoded.gz"

import gzip
vocabulary={}

question_anslabel_raw_100=["InsuranceQA.question.anslabel.raw.100.pool.solr.train.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.100.pool.solr.valid.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.100.pool.solr.test.encoded.gz"]
question_anslabel_raw_500=["InsuranceQA.question.anslabel.raw.500.pool.solr.train.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.500.pool.solr.test.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.500.pool.solr.valid.encoded.gz"]
question_anslabel_raw_1000=["InsuranceQA.question.anslabel.raw.1000.pool.solr.train.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.1000.pool.solr.valid.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.1000.pool.solr.test.encoded.gz"]
question_anslabel_raw_1500=["InsuranceQA.question.anslabel.raw.1500.pool.solr.train.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.1500.pool.solr.valid.encoded.gz",
                            "InsuranceQA.question.anslabel.raw.1500.pool.solr.test.encoded.gz"]


def load_vocab():
    with open(os.path.join(curdir, 'data', 'V2', 'vocabulary'), 'r') as f:
        for x in f.readlines():
            y = x.split()
            print("id: %s, word: %s" % (y[0], y[1:]))
            # assert len(y) == 2, "vocabulary item is not two. raw: %s lis: %s" % (x, y)
            vocabulary[y[0].strip()] = reduce(lambda x,z: x + " " + z.strip() ,y[1:], '')
    print("Got %d items" % len(vocabulary.keys()))

load_vocab()

def load_label_to_ans(file_path = os.path.join(curdir, label2answer)):
    index = 0
    label2answer_json = {}
    
    with gzip.open(file_path, 'r') as fin:
        for line in fin:
            print("index %d %s" % (index, line))
            line = line.decode().split('\t')
            AnswerLabel=line[0]
            AnswerText=line[1]
            index += 1
            label2answer_json[AnswerLabel] = dict({
                "text": reduce(lambda x,y: x+" "+ vocabulary[y],AnswerText.split(), ""),
                "tokens": AnswerText.split()
            })

    with open(os.path.join(curdir, os.path.basename(file_path)) + '.json', "w") as fout:
        json.dump(label2answer_json, fout, ensure_ascii=False)

def read_question_anslabel_raw(file_path, result):
    index = 0
    with gzip.open(file_path, 'r') as fin:
        for line in fin:
            # print('line split: %s' % line.split('\t'))
            t = line.decode().split('\t')
            print(len(t))
            assert len(t) == 4, "wrong length of question and answer uttrance"
            Domain = t[0]
            QUESTION = t[1]
            Groundtruth = t[2]
            Pool = t[3]
            print("Domain", Domain)
            print("QUESTION ids:", QUESTION)
            # print("QUESTION", reduce(lambda x,y: x+" "+vocabulary[y], QUESTION.split(), ""))
            print("Groundtruth", Groundtruth)
            print("Pool", Pool)
            result[index] = {
                "domain": Domain,
                "question_en": reduce(lambda x,y: x+" "+vocabulary[y], QUESTION.split(), ""),
                "ground_truth": Groundtruth.split(),
                "pool": Pool.split()
            }

            index += 1

    return result

def parse_all_raw_data():
    for x in question_anslabel_raw_100:
        result = {}
        read_question_anslabel_raw('data/V2/' + x, result)
        with open(os.path.join(curdir, os.path.basename(x)) + '.json', "w") as fout:
            json.dump(result, fout, ensure_ascii=False)

    # for x in question_anslabel_raw_500:
    #     result = {}
    #     read_question_anslabel_raw('data/V2/' + x, result)
    #     with open(os.path.join(curdir, os.path.basename(x)) + '.json', "w") as fout:
    #         json.dump(result, fout, ensure_ascii=False)

    # for x in question_anslabel_raw_1000:
    #     result = {}
    #     read_question_anslabel_raw('data/V2/' + x, result)        
    #     with open(os.path.join(curdir, os.path.basename(x)) + '.json', "w") as fout:
    #         json.dump(result, fout, ensure_ascii=False)

    # for x in question_anslabel_raw_1500:
    #     result = {}
    #     read_question_anslabel_raw('data/V2/' + x, result)    
    #     with open(os.path.join(curdir, os.path.basename(x)) + '.json', "w") as fout:
    #         json.dump(result, fout, ensure_ascii=False)

def main():
    # load_label_to_ans()
    # read_question_anslabel_raw()
    parse_all_raw_data()
    pass


if __name__ == '__main__':
    main()
