import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

def toGray(img, luminance=False):
    if luminance:
        params = [0.299, 0.589, 0.144]
    else:
        params = [0.2125, 0.7154, 0.0721]
    grayImg = np.ceil(np.dot(img[...,:3], params))
    return grayImg

def toBinary(img, threshold = 90):
    img = toGray(img)
    binaryImg = np.where(img > threshold, 1, 0)
    return binaryImg


face = scipy.misc.face()
plt.imshow(face, cmap='gray')
plt.show()
faceGray = toGray(face)
plt.imshow(faceGray, cmap='gray')
plt.show()
faceBlack = toBinary(face)
plt.imshow(faceBlack, cmap='gray')
plt.show()