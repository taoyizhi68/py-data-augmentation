## py-data-augmentation
Image data augmentation for learning algorithm. This repo is highly based on takmin's c++
[version](https://github.com/takmin/DataAugmentation).

## Installation Dependencies:

* Python 2.7
* numpy
* scikit-image

You can install with pip or just clone the repo:

```
pip install pydaag
```

## How to use:
Your input images should have shape like (img_numbers, img_rows, img_cols, img_channels).

If input images are grayscale, then the shape should be (img_numbers, img_rows, img_cols).

Simple example:
```
from pydaag import pydaag

#######################################################################
inputs:
	images: input images
	x_slide: Maximum slide in X direction, it's ratio of width of image.
	y_slide: Maximum slide in Y direction, it's ratio of height of image.
	z_rotateion: Maximum rotation around Z axis.
	y_rotateion: Maximum rotation around Y axis.
	x_rotateion: Maximum rotation around X axis.
	blur_max_sigma: Maximum standard deviation of Gaussian blur.
	noise_max_sigma: Maximum standard deviation of Gaussian noise
#######################################################################
images_ = pydaag.data_augmentation(images, x_slide=0.2, y_slide=0.2, 
                                   z_rotation=20, y_rotation=20, x_rotation=20, 
                                   blur_max_sigma=3, noise_max_sigma=20)
```
You can find an example in test/test.py.

Run the test file:
```
git clone https://github.com/taoyizhi68/py-data-augmentation.git
cd py-data-augmentation\test
python test.py
```

**inputs:**

![](https://github.com/taoyizhi68/py-data-augmentation/blob/master/test/img/input.png "inputs")

**outputs:**

![](https://github.com/taoyizhi68/py-data-augmentation/blob/master/test/img/output.png "outputs")