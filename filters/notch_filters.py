import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from math import exp, pow

class IdealNotchFilter:
    def __init__(self):
        pass
    
    def apply_filter(self, fshift, points, d0, path):
        m = fshift.shape[0]
        n = fshift.shape[1]
        for u in range(m):
            for v in range(n):
                for d in range(len(points)):
                    u0 = points[d][0]
                    v0 = points[d][1]
                    u0, v0 = v0, u0
                    d1 = pow(pow(u - u0, 2) + pow(v - v0, 2), 1)
                    d2 = pow(pow(u + u0, 2) + pow(v + v0, 2), 1)
                    if d1 <= d0 or d2 <= d0:
                        fshift[u][v] *= 0.0
        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        matplotlib.image.imsave(path, img_back, cmap = "gray")
        return

class ButterworthNotchFilter:
    def __init__(self):
        pass
    
    def apply_filter(self, fshift, points, d0, path, order = 1):
        m = fshift.shape[0]
        n = fshift.shape[1]
        for u in range(m):
            for v in range(n):
                for d in range(len(points)):
                    u0 = points[d][0]
                    v0 = points[d][1]
                    u0, v0 = v0, u0
                    d1 = pow(pow(u - u0, 2) + pow(v - v0, 2), 0.5)
                    d2 = pow(pow(u + u0, 2) + pow(v + v0, 2), 0.5)
                    fshift[u][v] *= (1.0 / (1 + pow((d0 * d0) / (d1 * d2), order))) 
                    
        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        matplotlib.image.imsave(path, img_back, cmap = "gray")
        return
    
class GaussianNotchFilter:
    def __init__(self):
        pass
    
    def apply_filter(self, fshift, points, d0, path):
        m = fshift.shape[0]
        n = fshift.shape[1]
        for u in range(m):
            for v in range(n):
                for d in range(len(points)):
                    u0 = points[d][0]
                    v0 = points[d][1]
                    u0, v0 = v0, u0
                    d1 = pow(pow(u - u0, 2) + pow(v - v0, 2), 0.5)
                    d2 = pow(pow(u + u0, 2) + pow(v + v0, 2), 0.5)
                    fshift[u][v] *= (1 - exp(-0.5 * (d1 * d2 / pow(d0, 2))))

        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        matplotlib.image.imsave(path, img_back, cmap = "gray")
        return
