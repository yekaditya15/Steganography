import cv2, numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import scipy.fft

def det(img):
    img = cv2.imread(img)
    img = img.reshape(-1)
    det = img & 3
    dec = det
    dec = (det[::3] << 6) | (det[1::3] << 4) | (det[2::3] << 2)
    return dec

def plot(*imgs):
    # plotting spatial domain, channelwise
    offset = 0
    channel = 3
    offset = offset%3+channel
    for i in imgs:
        plt.plot(i[offset:offset + 10000:3])
    plt.show()

    # applying fast fourier transform
    for i in imgs:
        plt.plot(np.fft.fft(i))
    plt.show()

    # applying discrete cosine transform
    for i in imgs:
        # plt.plot(scipy.fft.dct(i))
        mag = np.abs(scipy.fft.dct(i))
        i = mag # delete thissssssssssssssssssssssssssssssssss
        mean = np.mean(mag)
        std_dev = np.std(mag)
        thresh = mean + 3*std_dev
        arr = np.zeros_like(mag)
        arr[mag > thresh] = 1
        arr1 = np.diff(arr)
        plt.plot(arr1)
        plt.show()

        c_max_index = scipy.signal.find_peaks(i)
        plt.plot(i)
        plt.scatter(c_max_index[0],i[c_max_index[0]],linewidth=0.3, s=50, c='r')
        plt.show()


        # dft_output = np.fft.fft(i)  # DFT output
        # plt.plot(dft_output)
        # plt.show()
        # sampling_function = dirac_delta(np.arange(len(dft_output)), 1000000)  # Sampling function
        # delta_output = np.convolve(dft_output, sampling_function, mode='same')  # Convolution
        # plt.plot(delta_output)
        # plt.show()

    #plt.show()


def dirac_delta(n, k):
    global i
    i+=1
    print(i)
    """Approximation of Dirac delta function"""
    delta = np.zeros_like(n)
    delta[k] = 1.0
    return delta

i = 0
img0 = det('embedded/c08_c01.png')
# img1 = det('embedded/enc1.png')
# img2 = det('embedded/enc2.png')
plot(img0)