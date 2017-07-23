import numpy as np
import skimage as skimage
from skimage import data, io, filters, transform
from rotate import rotate

def guassian_blur(images, blur_max_sigma):
	for i in xrange(images.shape[0]):
		blur_sigma = np.random.uniform(0, blur_max_sigma)
		if blur_sigma > 0:
			images[i] = skimage.filters.gaussian(images[i], sigma=blur_sigma, multichannel=True)

def gaussian_noise(images, noise_max_sigma, img_rows, img_cols, img_channels):
	scale_ratio = 255. / np.max(images[0])
	if img_channels > 1:
		noise_shape = (img_rows, img_cols, img_channels)
	else:
		noise_shape = (img_rows, img_cols)
	for i in xrange(images.shape[0]):
		noise_sigma = np.random.uniform(0, noise_max_sigma)
		gaussian_noise = np.random.normal(loc=0, scale=noise_sigma, size=noise_shape)
		images[i] = images[i] * scale_ratio + gaussian_noise
		images[i][images[i]>255] = 255
		images[i][images[i]<0] = 0
		images[i] = images[i] / scale_ratio

def slide(images, img_rows, img_cols, x_max_slide, y_max_slide):
	assert(x_max_slide > 0)
	assert(y_max_slide > 0)
	if x_max_slide > 1:
		x_max_slide = 1
	if y_max_slide > 1:
		y_max_slide = 1

	x_max_slide *= float(img_cols)
	y_max_slide *= float(img_rows)
	for i in xrange(images.shape[0]):
		x_slide = np.random.uniform(-x_max_slide, x_max_slide)
		y_slide = np.random.uniform(-y_max_slide, y_max_slide)

		x_b, x_e = 0, img_cols
		y_b, y_e = 0, img_rows
		if x_slide > 0:
			x_e -= x_slide
		else:
			x_b -= x_slide
		if y_slide > 0:
			y_e -= y_slide
		else:
			y_b -= y_slide

		temp = images[i, int(y_b):int(y_e), int(x_b):int(x_e)]
		images[i] = transform.resize(temp, (img_rows, img_cols))

def data_augmentation(images, x_slide=None, y_slide=None, 
					  z_rotation=0, y_rotation=0, x_rotation=0, 
					  blur_max_sigma=None, noise_max_sigma=None):
	
	assert(len(images.shape) > 2)

	data_type = images.dtype
	batch_size = images.shape[0]
	img_rows, img_cols = images.shape[1], images.shape[2]
	if len(images.shape) == 4:
		img_channels = images.shape[3]
	else:
		img_channels = 1

	rst = np.copy(images)
	rst = rst.astype(float)

	#slide
	if x_slide > 0 or y_slide > 0:
		slide(rst, img_rows, img_cols, x_slide, y_slide)

	#rotate
	if x_rotation > 0 or y_rotation > 0 or z_rotation > 0:
		rotate(rst, x_rotation, y_rotation, z_rotation, img_rows, img_cols)

	#gaussian_blur
	if blur_max_sigma > 0:
		guassian_blur(rst, blur_max_sigma)

	#Add noise
	if noise_max_sigma > 0:
		gaussian_noise(rst, noise_max_sigma, img_rows, img_cols, img_channels)

	rst = rst.astype(data_type)
	return rst
