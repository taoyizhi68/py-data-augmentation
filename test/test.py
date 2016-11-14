import numpy as np
import matplotlib.pyplot as plt
import skimage as skimage
from skimage import data, io, filters, transform
from pydaag import pydaag
plt.rcParams['figure.figsize'] = (10, 10)

images = np.zeros((5, 256, 256, 3))
for i in range(5):
    filename = 'img\\%d.jpg'%(i+1)
    image = skimage.data.imread(filename, as_grey=0)
    image = skimage.transform.resize(image, (256, 256, 3))
    images[i] = image

for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(images[i])
    plt.axis('off')
plt.show()

images_ = pydaag.data_augmentation(images, x_slide=0.2, y_slide=0.2, 
                                   z_rotation=20, y_rotation=20, x_rotation=20, 
                                   blur_max_sigma=3, noise_max_sigma=20)
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(images_[i])
    plt.axis('off')
plt.show()