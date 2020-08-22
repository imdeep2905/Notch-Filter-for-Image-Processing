import cv2
import numpy as np
from matplotlib import pyplot as plt


class notchFilter:
    def __init__(self):
        pass
    def applyFilter(self,path,x,y):
        img = cv2.imread(path,0)

        # Fourier transform
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        plt.imshow(magnitude_spectrum, cmap = 'gray')
        plt.show()

        #Apply filter
        for i in range(fshift.shape[0]):
            for j in range(fshift.shape[1]):
                for k in range(6):
                    m = x[k]
                    n = y[k]
                    if(((m - j)*(m-j) )+((n - i)*(n-i)) < 121):
                        fshift[i][j] = 0


        f_ishift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        plt.imshow(img_back,cmap= 'gray')
        plt.show()


if __name__ == "__main__":
    j = notchFilter()
    j.applyFilter('  ',[100,135,125,115,150,125],[50,50,44,149,150,156])


              
'''
list for image 13
x = [100,135,125,115,150,125]
y = [50,50,44,149,150,156]
100
50
135
50
125
44
115
149
150
150
125
156


a.png points
97 40
197 40
97 79
100 158
100 200
197 79
201 155
200 198

'''