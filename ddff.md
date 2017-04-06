---
layout: default
title: Deep Depth From Focus
show-avatar: false
published: true
---

<center><font size="7"><b>Deep Depth From Focus</b></font></center>
<hr  width="80%" size="1"/>
<center><font size="5">Caner Hazirbas, Laura Leal-Taixé, Daniel Cremers</font></center>

<div style="text-align: justify">
<img src="https://hazirbas.github.io/img/ddffnet.png">
</div>

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
