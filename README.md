[![PyPI](https://img.shields.io/pypi/v/insuranceqa_data.svg)](https://pypi.python.org/pypi/insuranceqa_data) [![PyPI download month](https://img.shields.io/pypi/dm/insuranceqa_data.svg)](https://pypi.python.org/pypi/insuranceqa_data/) [![](https://img.shields.io/pypi/pyversions/insuranceqa_data.svg)](https://pypi.org/pypi/insuranceqa_data/) [![PyPI version shields.io](https://img.shields.io/pypi/v/insuranceqa_data.svg)](https://pypi.python.org/pypi/insuranceqa_data/) [![License](https://cdndownload2.chatopera.com/cskefu/licenses/chunsong1.0.svg)](https://www.cskefu.com/licenses/v1.html "开源许可协议") [![](https://img.shields.io/pypi/format/insuranceqa_data.svg)](https://pypi.org/pypi/insuranceqa_data/)

# 保险行业语料库

```
pip install -U insuranceqa_data
```

该语料库包含从网站[Insurance Library](http://www.insurancelibrary.com/) 收集的问题和答案。

据我们所知，这是保险领域首个开放的QA语料库：

* 该语料库的内容由现实世界的用户提出，高质量的答案由具有深度领域知识的专业人士提供。 所以这是一个具有真正价值的语料，而不是玩具。

* 在上述论文中，语料库用于答复选择任务。 另一方面，这种语料库的其他用法也是可能的。 例如，通过阅读理解答案，观察学习等自主学习，使系统能够最终拿出自己的看不见的问题的答案。

* 数据集分为两个部分“问答语料”和“问答对语料”。问答语料是从原始英文数据翻译过来，未经其他处理的。问答对语料是基于问答语料，又做了分词和去标去停，添加label。所以，"问答对语料"可以直接对接机器学习任务。如果对于数据格式不满意或者对分词效果不满意，可以直接对"问答语料"使用其他方法进行处理，获得可以用于训练模型的数据。

欢迎任何进一步增加此数据集的想法。

## 快速开始

依赖：

* Python: 2.x, 3.x
* Pip

### 1/2 安装脚本包

```
pip install -U insuranceqa_data
```

### 2/2 安装语料包

进入[证书商店](https://store.chatopera.com/product/insqa001)，购买证书，购买后进入【证书-详情】，点击【复制证书标识】。

然后，设置环境变量 `INSQA_DL_LICENSE`，比如使用命令行终端：

```bash
# Linux / macOS
export INSQA_DL_LICENSE=YOUR_LICENSE
## e.g. if your license id is `FOOBAR`, run `export INSQA_DL_LICENSE=FOOBAR`

# Windows
set INSQA_DL_LICENSE=YOUR_LICENSE
```

最后，执行以下命令，完成数据的下载。

```bash
python -c "import insuranceqa_data; insuranceqa_data.download_corpus()"
```


## 数据格式

[问答对数据](https://github.com/chatopera/insuranceqa-corpus-zh/wiki/%E9%97%AE%E7%AD%94%E5%AF%B9%E6%95%B0%E6%8D%AE)

[问答数据](https://github.com/chatopera/insuranceqa-corpus-zh/wiki/%E9%97%AE%E7%AD%94%E8%AF%AD%E6%96%99)

## 机器学习项目

可将本语料库和以下开源码配合使用


[deep-qa-1](https://github.com/chatopera/insuranceqa-corpus-zh/tree/release/deep_qa_1): Baseline model

[InsuranceQA TensorFlow](https://github.com/l11x0m7/InsuranceQA_zh): CNN with TensorFlow

[n-grams-get-started](https://github.com/Samurais/n-grams-get-started): N元模型

[word2vec-get-started](https://github.com/Samurais/word2vec-get-started): 词向量模型


## 声明

声明1 : [insuranceqa-corpus-zh](https://github.com/chatopera/insuranceqa-corpus-zh)

本数据集使用翻译 [insuranceQA](https://github.com/shuzi/insuranceQA)而生成，代码发布证书 GPL 3.0。数据仅限于研究用途，如果在发布的任何媒体、期刊、杂志或博客等内容时，必须注明引用和地址。

```
InsuranceQA Corpus, Hai Liang Wang, https://github.com/chatopera/insuranceqa-corpus-zh, 07 27, 2017
```

任何基于[insuranceqa-corpus](https://github.com/chatopera/insuranceqa-corpus-zh)衍生的数据也需要开放并需要声明和“声明1”和“声明2”一致的内容。

声明2 : [insuranceQA](https://github.com/shuzi/insuranceQA)

此数据集仅作为研究目的提供。如果您使用这些数据发表任何内容，请引用我们的论文：[Applying Deep Learning to Answer Selection: A Study and An Open Task](https://arxiv.org/abs/1508.01585)。Minwei Feng, Bing Xiang, Michael R. Glass, Lidan Wang, Bowen Zhou @ 2015