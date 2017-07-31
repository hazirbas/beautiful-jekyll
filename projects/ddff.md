---
layout: page
title: Deep Depth From Focus
subtitle: Caner Hazirbas, Laura Leal-Taixé, Daniel Cremers
show-avatar: false
social-share: true
share-img: https://hazirbas.github.io/img/ddffteaser.png
published: true
---

![DDFFNet]({{site.baseurl}}/img/ddffnet.png){: .center-image }
<br>

<div style="text-align: justify">
Depth from Focus (DFF) is one of the classical ill-posed inverse problems in computer vision.
Most approaches recover the depth at each pixel based on the focal setting which exhibits maximal sharpness.
Yet, it is not obvious how to reliably estimate the sharpness level, particularly in low-textured areas.
In this paper, we propose `Deep Depth From Focus (DDFF)' as the first end-to-end learning approach to this problem.
Towards this goal, we create a novel real-scene indoor benchmark composed of 4D light-field images obtained from a plenoptic camera and ground truth depth obtained from a registered RGB-D sensor.
Compared to existing benchmarks our dataset is 30 times larger, enabling the use of machine learning for this inverse problem.
We compare our results with state-of-the-art DFF methods and we also analyze the effect of several key deep architectural components.
These experiments show that DDFFNet achieves state-of-the-art performance in all scenes, reducing depth error by more than 70% wrt classic DFF methods.
</div>

<div style="text-align: center">
<a href="https://arxiv.org/abs/1704.01085" target="_blank">
<button class="button buttonpaper"> arXiv </button>
</a>
<a href="https://arxiv.org/pdf/1704.01085" target="_blank">
<button class="button buttonpaper"> pdf </button>
</a>
</div>

### Bibtex
```
@inproceedings{hazirbas17ddff,
  title     = {Deep Depth From Focus},
  author    = {C. Hazirbas and L. Leal-Taixé and D. Cremers},
  booktitle = {Arxiv preprint arXiv:1704.01085},
  month     = {April},
  year      = {2017},
}
```

### Share on
{% include social-share.html %}
