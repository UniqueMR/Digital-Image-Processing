import cv2
import numpy as np

def imgEnhancement(img, laplace):
    row, col = img.shape
    new_img = np.zeros((row, col))
    for i in range(row - 2):
        for j in range(col - 2):
            # new_img[i+1, j+1] = abs(np.sum(img[i:i+3,j:j+3] * laplace))\
            #  + img[i+1,j+1]
            new_img[i+1, j+1] = abs(np.sum(img[i:i+3,j:j+3] * laplace))
    return np.uint8(new_img)

img = cv2.imread('../../img/laplace/f1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('../../img/laplace/grey.png', img)

# laplace = np.array([[0,1,0],[1,-4,1],[0,1,0]])
# laplace = np.array([[1,1,1],[1,-8,1],[1,1,1]])
laplace = np.array([[-1,2,-1],[2,-4,2],[-1,2,-1]])
img = imgEnhancement(img, laplace)
# cv2.imwrite('../../img/laplace/enhanced img1.png', img)
# cv2.imwrite('../../img/laplace/enhanced img2.png', img)
# cv2.imwrite('../../img/laplace/enhanced img3.png', img)
cv2.imwrite('../../img/laplace/edge3.png', img)