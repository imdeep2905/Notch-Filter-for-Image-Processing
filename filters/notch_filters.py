import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

class IdealNotchFilter:
    def __init__(self):
        pass
    
    def apply_filter(self, fshift, points, freq, path):
        #Apply filter
        for i in range(fshift.shape[0]):
            for j in range(fshift.shape[1]):
                for k in range(len(points)):
                    m = points[k][0]
                    n = points[k][1]
                    if(((m - j)*(m-j) )+((n - i)*(n-i)) < freq):
                        fshift[i][j] = 0

        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        matplotlib.image.imsave(path, img_back, cmap = "gray")
        return

class ButterworthNotchFilter:
    def __init__(self):
        pass
    
    def apply_filter(self, fshift, points, freq, path):
        #Apply filter
        for i in range(fshift.shape[0]):
            for j in range(fshift.shape[1]):
                for k in range(len(points)):
                    m = points[k][0]
                    n = points[k][1]
                    if(((m - j)*(m-j) )+((n - i)*(n-i)) < freq):
                        fshift[i][j] = 0

        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        matplotlib.image.imsave(path, img_back, cmap = "gray")
        return
    
class GaussianNotchFilter:
    def __init__(self):
        pass
    
    def apply_filter(self, fshift, points, freq, path):
        #Apply filter
        for i in range(fshift.shape[0]):
            for j in range(fshift.shape[1]):
                for k in range(len(points)):
                    m = points[k][0]
                    n = points[k][1]
                    if(((m - j)*(m-j) )+((n - i)*(n-i)) < freq):
                        fshift[i][j] = 0

        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        matplotlib.image.imsave(path, img_back, cmap = "gray")
        return
