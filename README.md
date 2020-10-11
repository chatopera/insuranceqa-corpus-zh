[![chatoper banner][co-banner-image]][co-url]

[co-banner-image]: https://user-images.githubusercontent.com/3538629/42383104-da925942-8168-11e8-8195-868d5fcec170.png
[co-url]: https://www.chatopera.com

# 保险行业语料库
[详细文档](https://github.com/Samurais/insuranceqa-corpus-zh/wiki)

# 大家怎么说

> 看了下您的项目，我觉得这份数据可以用于保险领域的中文问答研究，对于较短的问题翻译很准确，长度较长的答案翻译就有些不连贯的问题，大体上关键词信息和一些上下文信息都有，我觉得是份很好的中文语料。 - [fssqawj](https://github.com/fssqawj), East China Normal University

> Excellent work! - [rgtjf](https://github.com/rgtjf), East China Normal University

# 基线

Baseline model for [insuranceqa-corpus-zh](https://github.com/Samurais/insuranceqa-corpus-zh/wiki) 

mini-batch size = 100, hidden_layers = [100, 50], lr = 0.0001.

![](./deep_qa_1/baseline_acc.png)

![](./deep_qa_1/baseline_loss.png)

> Epoch 25, total step 36400, accuracy 0.9031, cost 1.056221.

## Deps
Python3+

```
pip install -r Requirements.txt
```

## Run
A very simple network as baseline model.
```
python3 deep_qa_1/network.py
python3 visual/accuracy.py
python3 visual/loss.py
```

下载[文档](./deep_qa_1/baseline_article.pdf)了解更多关于DeepQA-1的实现和Baseline。

## 声明

声明1 : [insuranceqa-corpus-zh](https://github.com/Samurais/insuranceqa-corpus-zh)

本数据集使用翻译 [insuranceQA](https://github.com/shuzi/insuranceQA)而生成，代码发布证书 GPL 3.0。数据仅限于研究用途，如果在发布的任何媒体、期刊、杂志或博客等内容时，必须注明引用和地址。

```
InsuranceQA Corpus, Hai Liang Wang, https://github.com/Samurais/insuranceqa-corpus-zh, 07 27, 2017
```

任何基于[insuranceqa-corpus](https://github.com/Samurais/insuranceqa-corpus-zh)衍生的数据也需要开放并需要声明和“声明1”和“声明2”一致的内容。

声明2 : [insuranceQA](https://github.com/shuzi/insuranceQA)

此数据集仅作为研究目的提供。如果您使用这些数据发表任何内容，请引用我们的论文：[Applying Deep Learning to Answer Selection: A Study and An Open Task](https://arxiv.org/abs/1508.01585)。Minwei Feng, Bing Xiang, Michael R. Glass, Lidan Wang, Bowen Zhou @ 2015


## Chatopera 云服务

[https://bot.chatopera.com/](https://bot.chatopera.com/)

[Chatopera 云服务](https://bot.chatopera.com)是一站式实现聊天机器人的云服务，按接口调用次数计费。Chatopera 云服务是 [Chatopera 机器人平台](https://docs.chatopera.com/products/chatbot-platform/index.html)的软件即服务实例。在云计算基础上，Chatopera 云服务属于**聊天机器人即服务**的云服务。

Chatopera 机器人平台包括知识库、多轮对话、意图识别和语音识别等组件，标准化聊天机器人开发，支持企业 OA 智能问答、HR 智能问答、智能客服和网络营销等场景。企业 IT 部门、业务部门借助 Chatopera 云服务快速让聊天机器人上线！

<details>
<summary>展开查看 Chatopera 云服务的产品截图</summary>
<p>

<p align="center">
  <b>自定义词典</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530072-da92d600-d33e-11e9-8656-01c26caff4f9.png" width="800">
</p>

<p align="center">
  <b>自定义词条</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530091-e41c3e00-d33e-11e9-9704-c07a2a02b84e.png" width="800">
</p>

<p align="center">
  <b>创建意图</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530169-12018280-d33f-11e9-93b4-9db881cf4dd5.png" width="800">
</p>

<p align="center">
  <b>添加说法和槽位</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530187-20e83500-d33f-11e9-87ec-a0241e3dac4d.png" width="800">
</p>

<p align="center">
  <b>训练模型</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530235-33626e80-d33f-11e9-8d07-fa3ae417fd5d.png" width="800">
</p>

<p align="center">
  <b>测试对话</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530253-3d846d00-d33f-11e9-81ea-86e6d47020d8.png" width="800">
</p>

<p align="center">
  <b>机器人画像</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530312-6442a380-d33f-11e9-869c-85fb6a835a97.png" width="800">
</p>

<p align="center">
  <b>系统集成</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530281-4ecd7980-d33f-11e9-8def-c53251f30138.png" width="800">
</p>

<p align="center">
  <b>聊天历史</b><br>
  <img src="https://static-public.chatopera.com/assets/images/64530295-5856e180-d33f-11e9-94d4-db50481b2d8e.png" width="800">
</p>

</p>
</details>


<p align="center">
  <b>立即使用</b><br>
  <a href="https://bot.chatopera.com" target="_blank">
      <img src="https://static-public.chatopera.com/assets/images/64531083-3199aa80-d341-11e9-86cd-3a3ed860b14b.png" width="800">
  </a>
</p>
