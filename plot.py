import cv2, numpy as np
import matplotlib.pyplot as plt
import matplotlib as mt
import scipy.fft
from detecta import detect_peaks
import glob
import os

def det(img):
    img = cv2.imread(img)
    img = img.reshape(-1)
    det = img & 3
    dec = det
    dec = (det[::3] << 6) | (det[1::3] << 4) | (det[2::3] << 2)
    return dec

def plot(name, opath, *imgs):
    # plotting Spatial domain, channelwise
    offset = 0
    channel = 3
    offset = offset%3+channel
    for i in imgs:
        x = i[offset:offset + 10000:3]
        #plt.plot(x)
        k = detect_peaks(x, mpd=10, show=True, title=None)
        
        plt.plot(k, k[x], marker='+', markersize=10, color='r', linestyle='None')
        #plt.plot(x)


       # plt.axhline(np.mean(i[offset:offset + 10000:3]), color='r')
        #plt.axhline(y=mean, color='r', linestyle='--', linewidth=2)
   # plt.savefig(opath + '' +name)
    plt.show()
    plt.clf()

    # applying discrete cosine transform
    # for i in imgs:
    #     plt.plot(scipy.fft.dct(i))
    # # plt.show()
    # # plt.savefig(opath+ 'p3_'+name)
    # plt.clf()


for i in glob.glob('embedded\c08_c03*'):
    print("Current Image:", i)
    img0 = det(i)
    # img1 = det('embedded/enc1.png')
    # img2 = det('embedded/enc2.png')
    plot(os.path.basename(i), 'test_1/', img0)