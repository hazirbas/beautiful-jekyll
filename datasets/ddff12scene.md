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
<div style="text-align: center">
<a href="https://competitions.codalab.org/competitions/17807" target="_blank">
<button class="button buttonpaper"> >> Depth From Focus Competition on the DDFF 12-Scene Dataset << </button>
</a>
</div>
DDFF 12-Scene dataset consists of 720 lightfield images and coregistered depth maps.
<ul style="line-height:2">
<li><b>Lightfield</b>: 4D lightfield images; each of which has 9 × 9 × 383 × 552 undistorted subapertures Images are saved as numpy arrays and can be loaded as follows:
{% highlight python %}
import numpy as np
lf = np.load('LF_0001.npy')
{% endhighlight %}
</li>
<li><b>Lightfield-mat</b>: 4D lightfield images in Matlab format
</li>
<li><b>DepthRegistered</b>: registered depth maps; recorded in meters and scaled by a factor of 1000. Depth images are saved in uint16 bits and only available for "train" set:
{% highlight python %}
import cv2
from PIL import Image
# in meters
depth = cv2.imread('DEPTH_0001.png', cv2.IMREAD_ANYDEPTH) * 0.001
depth = np.array(Image.open('DEPTH_0001.png'), dtype=np.float) * 0.001
{% endhighlight %}
</li>
<li><b>RawImage</b>: raw images consist of Lytro ILLUM RAW formatted images
</li>
<li><b>LF CalibPattern</b>: calibration pattern for the Lytro ILLUM camera
</li>
<li><b>WhiteImages</b>: white images required by the Lytro Desktop
</li>
</ul>

<div style="text-align: left">
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield.tar.gz">
<button class="button buttonpaper">Lightfield [24.5GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield-mat.tar.gz">
<button class="button buttonpaper">Lightfield-mat [23.9GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/depthregistered.tar.gz">
<button class="button buttonpaper">DepthRegistered [57.9MB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/rawimage.tar.gz">
<button class="button buttonpaper">RawImage [29.7GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lytrocalibpattern.tar.gz">
<button class="button buttonpaper">LF CalibPattern [2.3GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/B5143904760.tar.gz">
<button class="button buttonpaper">LF WhiteImages [1.5GB]</button>
</a>
</div>

### License
All data in the DDFF 12-Scene benchmark is licensed under a [Creative Commons 4.0 Attribution License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/){:target="_blank"}.

### Log
[07-12-2017] -- Lighfield images in Matlab format<br>
[05-12-2017] -- Lighfield calibration pattern and white images<br>
[15-09-2017] -- Lightfield images, registered depth maps and raw Lytro ILLUM images

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