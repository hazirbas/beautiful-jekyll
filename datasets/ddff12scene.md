---
layout: page
title: DDFF 12-Scene
subtitle: 4.5D Lightfield-Depth Benchmark
show-avatar: false
social-share: true
share-img: https://hazirbas.github.io/img/ddff12scene.png
published: true
---

![DDFF12Scene]({{site.baseurl}}/img/ddff12scene.png){: .center-image }
<br>

Dataset consists of 720 lightfield images, each of which has 9 × 9 undistorted subapertures and each subaperture has 383 × 552 image resolution. Lightfields are saved as numpy array and can be load with numpy.load() in Python. Registered depth images are saved as unsigned int 16 bits and only available for "train" set. Depth values are scaled with a factor of 1000.

<div style="text-align: center">
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield.tar.gz">
<button class="button buttonpaper">lighfield.tar.gz [24.5GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/depthregistered.tar.gz">
<button class="button buttonpaper">depthregistered.tar.gz [57.9MB]</button>
</a>
</div>

### Log
[15/09/2017] -- Lightfield images along with registered depth maps are online.

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
