import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fftshift, ifftshift, fftn, ifftn, fft2
import os
import sys

path = sys.argv[1]
if os.path.exists(path):
    print(os.path.basename(path))
    img = cv2.imread(path,0)
    dim = range(img.ndim)
    k = fftshift(fftn(ifftshift(img, axes=dim), s=None, axes=dim), axes=dim)
    k /= np.sqrt(np.prod(np.take(img.shape, dim)))
    k = np.real(k)
    magnitude_spectrum = 20*np.log(np.abs(k)+1)
    plt.subplot(121),plt.imshow(img, cmap = 'gray', interpolation='nearest')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray' ,interpolation='nearest')
    plt.title('K-Space'), plt.xticks([]), plt.yticks([])
    plt.show()

