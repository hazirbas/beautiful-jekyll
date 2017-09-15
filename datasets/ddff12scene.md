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

<div style="text-align: justify">
Dataset consists of 720 lightfield images, each of which has 9 × 9 undistorted subapertures and each subaperture has 383 × 552 image resolution. Lightfields are saved as numpy array and can be loaded with numpy.load() in Python. Registered depth images are saved as unsigned int 16 bits and only available for "train" set. Depth values are scaled with a factor of 1000. Raw images consist of Lytro ILLUM RAW formatted images, can be used with Lytro Desktop or Lytro Power Tools.
</div>

<div style="text-align: center">
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield.tar.gz">
<button class="button buttonpaper">Lightfield [24.5GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/depthregistered.tar.gz">
<button class="button buttonpaper">DepthRegistered [57.9MB]</button>
</a>
</div>
<div style="text-align: center">
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/rawimage.tar.gz">
<button class="button buttonpaper">RawImage [29.7GB]</button>
</a>
</div>

### Log
[15-09-2017] -- Lightfield images along with registered depth maps and raw Lytro ILLUM images are online.

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
