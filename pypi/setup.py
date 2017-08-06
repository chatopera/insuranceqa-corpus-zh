# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
insuranceqa-corpus-zh
=====================

保险行业语料库

Welcome
-------

该语料库包含从网站\ `Insurance
Library <http://www.insurancelibrary.com/>`__ 收集的问题和答案。

据我们所知，这是保险领域首个开放的QA语料库：

-  该语料库的内容由现实世界的用户提出，高质量的答案由具有深度领域知识的专业人士提供。
   所以这是一个具有真正价值的语料，而不是玩具。

-  在上述论文中，语料库用于答复选择任务。
   另一方面，这种语料库的其他用法也是可能的。
   例如，通过阅读理解答案，观察学习等自主学习，使系统能够最终拿出自己的看不见的问题的答案。

欢迎任何进一步增加此数据集的想法。

语料数据
--------

+--------+----------+----------+----------------+
| -      | 问题     | 答案     | 词汇（英语）   |
+========+==========+==========+================+
| 训练   | 12,889   | 21,325   | 107,889        |
+--------+----------+----------+----------------+
| 验证   | 2,000    | 3354     | 16,931         |
+--------+----------+----------+----------------+
| 测试   | 2,000    | 3308     | 16,815         |
+--------+----------+----------+----------------+

每条数据包括问题的中文，英文，答案的正例，答案的负例。案的正例至少1项，基本上在\ *1-5*\ 条，都是正确答案。答案的负例有\ *200*\ 条，负例根据问题使用检索的方式建立，所以和问题是相关的，但却不是正确答案。

::

    {
        "INDEX": {
            "zh": "中文",
            "en": "英文",
            "domain": "保险种类",
            "answers": [""] # 答案正例列表
            "negatives": [""] # 答案负例列表
        },
        more ...
    }

-  训练：\ ``corpus/train.json``

-  验证：\ ``corpus/valid.json``

-  测试：\ ``corpus/test.json``

-  答案：\ ``corpus/answers.json`` 一共有 27,413 个回答，数据格式为
   ``json``:

   ::

       {
       "INDEX": {
           "zh": "中文",
           "en": "英文"
       },
       more ...
       }

中英文对照文件
~~~~~~~~~~~~~~

问答对
^^^^^^

::

    格式 INDEX ++$++ 保险种类 ++$++ 中文 ++$++ 英文

``corpus/train.txt``, ``corpus/valid.txt``, ``corpus/test.txt``.

答案
^^^^

::

    格式 INDEX ++$++ 中文 ++$++ 英文

``corpus/answers.txt``

快速开始
--------

在Python环境中，使用pip安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    pip install --upgrade insuranceqa_data

    import insuranceqa_data as insuranceqa
    train_data = insuranceqa.load_train()
    test_data = insuranceqa.load_train()
    valid_data = insuranceqa.load_train()

    # valid_data, test_data and train_data share the same properties
    for x in train_data:
        print('index %s value: %s ++$++ %s ++$++ %s' %
         (x, d[x]['zh'], d[x]['en'], d[x]['answers'], d[x]['negatives']))

    answers_data = insuranceqa.load_answers()
    for x in answers_data:
        print('index %s: %s ++$++ %s' % (x, d[x]['zh'], d[x]['en']))

声明
----

声明1 :
`insuranceqa-corpus-zh <https://github.com/Samurais/insuranceqa-corpus-zh>`__

本数据集使用翻译
`insuranceQA <https://github.com/shuzi/insuranceQA>`__\ 而生成，代码发布证书
GPL
3.0。数据仅限于研究用途，如果在发布的任何媒体、期刊、杂志或博客等内容时，必须注明引用和地址。

::

    InsuranceQA Corpus, Hai Liang Wang, https://github.com/Samurais/insuranceqa-corpus-zh, 07 27, 2017

任何基于\ `insuranceqa-corpus <https://github.com/Samurais/insuranceqa-corpus-zh>`__\ 衍生的数据也需要开放并需要声明和“声明1”和“声明2”一致的内容。

声明2 : `insuranceQA <https://github.com/shuzi/insuranceQA>`__

此数据集仅作为研究目的提供。如果您使用这些数据发表任何内容，请引用我们的论文：\ `Applying
Deep Learning to Answer Selection: A Study and An Open
Task <https://arxiv.org/abs/1508.01585>`__\ 。Minwei Feng, Bing Xiang,
Michael R. Glass, Lidan Wang, Bowen Zhou @ 2015
"""

setup(name='insuranceqa_data',
      version='2.0',
      description='Insuranceqa Corpus in Chinese for Machine Learning',
      long_description=LONGDOC,
      author='Hai Liang Wang',
      author_email='hailiang.hl.wang@gmail.com',
      url='https://github.com/Samurais/insuranceqa-corpus-zh',
      license="GPL 3.0",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'
      ],
      keywords='corpus,machine-learning,deep-learning,NLP,question-answering',
      packages= find_packages(),
      # package_dir={'insuranceqa_data':['insuranceqa_data']},
      package_data={'insuranceqa_data':['**/*md', 'LICENSE']}
)
