---
layout: page
title: TUM-LSI
subtitle: A Large-Scale Indoor Dataset
show-avatar: false
social-share: true
share-img:
published: true
---

<div style="text-align: center">
<a href="https://github.com/NavVisResearch/NavVis-Indoor-Dataset/" target="_blank">
<button class="button buttonpaper">TUM LSI Dataset</button>
</a>
<a href="{{site.baseurl}}/datasets/tum-lsi.zip">
<button class="button buttonpaper">Train/Test Splits</button>
</a>
</div>

### Note
The images in this dataset are all in portrait format, horizontal direction images were not rotated. By following PoseNet (ICCV, 2015) we first rescaled the images horizontally to 256 pixels, then did the random crops of size 224x224.

### Bibtex
```
@inproceedings{walch16spatialstms,
 author    = {F. Walch and C. Hazirbas and L. Leal-Taixé and T. Sattler and S. Hilsenbeck and D. Cremers},
 title     = {Image-based localization using LSTMs for structured feature correlation},
 booktitle = {ICCV},
 month     = {October},
 year      = {2017},
 }
```
