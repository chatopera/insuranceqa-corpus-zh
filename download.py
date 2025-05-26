#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2025 <> All Rights Reserved
#
#
# File: /c/Users/Administrator/chatopera/insuranceqa-corpus-zh/download.py
# Author: Hai Liang Wang
# Date: 2025-05-26:13:53:37
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2025-05-26:13:53:37"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

# 检查 Python 版本
if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

# 设置证书标识，购买自 https://store.chatopera.com/product/insqa001
os.environ["INSQA_DL_LICENSE"] = "YOUR LICENSE"
_licenseid = os.environ.get("INSQA_DL_LICENSE", None)
print("INSQA_DL_LICENSE=%s" % _licenseid)

# 初次下载数据
import insuranceqa_data
insuranceqa_data.download_corpus()


'''
使用 Pool data
'''
# 读取数据测试
train_data = insuranceqa_data.load_pool_train() # 训练集
test_data = insuranceqa_data.load_pool_test()   # 测试集
valid_data = insuranceqa_data.load_pool_valid() # 验证集
answers_data = insuranceqa_data.load_pool_answers()


# 打印 训练集 数据；测试集和验证集与 训练集 数据结构一致
for x in train_data:                       # 打印数据
    print('\n\nIndex %s \n question: %s' % \
     (x, train_data[x]['zh']))
    print(" answer: ")
    idx = 0
    for y in train_data[x]['answers']:
        idx += 1
        print("   %d. %s" % (idx, answers_data[y]["zh"]))