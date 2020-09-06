---
layout: page
title: DDFF 12-Scene
subtitle: 4.5D Lightfield-Depth Benchmark
show-avatar: false
social-share: true
share-img: https://hazirbas.github.io/assets/img/ddff12scene.png
published: true
---

![DDFF12Scene]({{site.baseurl}}/assets/img/ddff12scene.png){: .center-image }
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
<li><b>Depth</b>: registered depth maps; recorded in meters and scaled by a factor of 1000. Depth images are saved in uint16 bits and only available for "train" and "val" sets:
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
<li><b>CalibPattern</b>: calibration pattern for the Lytro ILLUM camera
</li>
<li><b>WhiteImages</b>: white images required by the Lytro Desktop
</li>
</ul>

<table class="borderless">
  <tr>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield.tar.gz">
      <button style="width:100%" class="button buttonpaper">Lightfield [24.5GB]</button></a>
    </td>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lightfield-mat.tar.gz">
      <button style="width:100%" class="button buttonpaper">Lightfield-mat [23.9GB]</button></a>
    </td>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/depthregistered.tar.gz">
      <button style="width:100%" class="button buttonpaper">Depth [57.9MB]</button></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/rawimage.tar.gz">
      <button style="width:100%" class="button buttonpaper">Raw Images [29.7GB]</button></a>
    </td>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/lytrocalibpattern.tar.gz">
      <button style="width:100%" class="button buttonpaper">CalibPattern [2.3GB]</button></a>
    </td>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/B5143904760.tar.gz">
      <button style="width:100%" class="button buttonpaper">WhiteImages [1.5GB]</button></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/ddff-dataset-trainval.h5">
      <button style="width:100%" class="button buttonpaper">DDFF Train [12.6GB]</button></a>
    </td>
    <td>
      <a href="https://vision.in.tum.de/webarchive/hazirbas/ddff12scene/ddff-dataset-test.h5">
      <button style="width:100%" class="button buttonpaper">DDFF Test [761.1MB]</button></a>
    </td>
  </tr>
</table>

<br>
### Depth From Focus Competition
Please submit your test results to <a href="https://competitions.codalab.org/competitions/17807" target="_blank">the DFF competition</a>.

### License
All data in the DDFF 12-Scene benchmark is licensed under a [Creative Commons 4.0 Attribution License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/){:target="_blank"}.

### Log
[24-04-2018] -- Trainval/Test hdf5 files added<br>
[07-12-2017] -- Lighfield images in Matlab format<br>
[05-12-2017] -- Lighfield calibration pattern and white images<br>
[15-09-2017] -- Lightfield images, registered depth maps and raw Lytro ILLUM images

### Bibtex
```
@InProceedings{hazirbas18ddff,
 author    = {C. Hazirbas and S. G. Soyer and M. C. Staab and L. Leal-Taixé and D. Cremers},
 title     = {Deep Depth From Focus},
 booktitle = {Asian Conference on Computer Vision (ACCV)},
 year      = {2018},
 month     = {December},
 eprint    = {1704.01085},
 url       = {https://hazirbas.com/projects/ddff/},
}
```

### Share on
{% include social-share.html %}
