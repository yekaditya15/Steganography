import cv2
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)

#open image file 
img = cv2.imread('a.bmp')

def get(img, k):
    imgr = img.copy()

    imgr = imgr[:,:,k]
    k = np.zeros((32,32))
    k[imgr == 255] = 1
    k[imgr == 0] = 0

    return k.reshape(-1)

# plt.plot(get(img,0), drawstyle='steps', color='red')
plt.plot(get(img,1), drawstyle='steps', color='green')
# plt.plot(get(img,2), drawstyle='steps', color='blue')

# Set the x-axis limits
plt.xlim(-1, 1024)

# Set the y-axis limits
plt.ylim(-0.1, 1.1)

# Add axis labels and title
plt.yticks([0, 1])
# add xticks, multiple os 32
plt.xticks(np.arange(0, 1025, 64)) 

# Show the plot
plt.show()

# print("\n\n")
# for i in range(32):
#     for j in range(32):
#         print(int(k[i][j]), end=' ')
#     print()
# print("\n\n")

# #show image
# cv2.imshow('image', k)
# cv2.waitKey(0)
