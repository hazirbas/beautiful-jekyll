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


DDFF 12-Scene dataset consists of in total 720
<ul style="line-height:2">
<li>4D lightfield images: each of which has 9 × 9 undistorted subapertures (383x552). Images are saved as a numpy array and can be loaded as follows:
{% highlight python %}
import numpy as np
lf = np.load('LF_0001.npy')
{% endhighlight %}
</li>
<li>registered depth maps: recorded in meters and scaled by a factor of 1000. Depth images are saved as unsigned int 16 bits and only available for "train" set.
{% highlight python %}
import cv2
from PIL import Image
# in meters
depth = cv2.imread('DEPTH_0001.png', cv2.IMREAD_ANYDEPTH) * 0.001
depth = np.array(Image.open('DEPTH_0001.png'), dtype=np.float) * 0.001
{% endhighlight %}
</li>
<li>raw images consist of Lytro ILLUM RAW formatted images.
</li>
<li>calibration files required by Lytro Desktop or Lytro Power Tools.
</li>
</ul>

<div style="text-align: center">
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield.tar.gz">
<button class="button buttonpaper">Lightfield [24.5GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/depthregistered.tar.gz">
<button class="button buttonpaper">DepthRegistered [57.9MB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/rawimage.tar.gz">
<button class="button buttonpaper">RawImage [29.7GB]</button>
</a>
<a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/B5143904760.tar.gz">
<button class="button buttonpaper">Lytro Calib [1.5GB]</button>
</a>
</div>

### License
All data in the DDFF 12-Scene benchmark is licensed under a [Creative Commons 4.0 Attribution License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/){:target="_blank"}.

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
