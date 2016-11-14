import numpy as np
from skimage import data, io, filters, transform

def rotate(images, x_max_rotation, y_max_rotation, z_max_rotation, img_rows, img_cols):
	assert(x_max_rotation >= 0)
	assert(y_max_rotation >= 0)
	assert(z_max_rotation >= 0)
	for i in xrange(images.shape[0]):
		x_rotation = np.random.uniform(-x_max_rotation, x_max_rotation) * np.pi / 180
		y_rotation = np.random.uniform(-y_max_rotation, y_max_rotation) * np.pi / 180
		z_rotation = np.random.uniform(-z_max_rotation, z_max_rotation) * np.pi / 180

		center_matrix1 = np.array([[1, 0, -img_cols/2.], 
								  [0, 1, -img_rows/2.],
								  [0, 0, 1]])

		R = np.dot(np.dot(z_matirx(z_rotation), y_matrix(y_rotation)), x_matrix(x_rotation))
		rotate_matrix = np.array([[R[0][0], R[0][1], 0], 
								  [R[1][0], R[1][1], 0],
								  [0,       0,       1]])
		#print rotate_matrix
		center_matrix2 = np.array([[1, 0, img_cols/2.], 
								  [0, 1, img_rows/2.],
								  [0, 0, 1]]) 

		center_trans1 = transform.AffineTransform(center_matrix1)
		rotate_trans = transform.AffineTransform(rotate_matrix)
		center_trans2 = transform.AffineTransform(center_matrix2)

		affine_trans = center_trans1 + rotate_trans + center_trans2
		images[i] = transform.warp(images[i], affine_trans, mode='edge')

def z_matirx(z):
	return np.array([[np.cos(z), -np.sin(z), 0],
		  			 [np.sin(z),  np.cos(z), 0],
		  			 [0,          0,         1]])
def y_matrix(y):
	return np.array([[np.cos(y),  0, np.sin(y)],
		  			 [0,          1, 0],
		  			 [-np.sin(y), 0, np.cos(y)]])
def x_matrix(x):
	return np.array([[1, 0,         0],
		  			 [0, np.cos(x), -np.sin(x)],
		  			 [0, np.sin(x), np.cos(x)]])