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

阅读 `详细文档 <https://github.com/Samurais/insuranceqa-corpus-zh>`__

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
      version='2.1',
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
