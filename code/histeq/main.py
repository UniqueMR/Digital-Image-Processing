from pickletools import uint8
from PIL import Image
from pylab import *
from numpy import *

def histeq(im, nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""
    imhist, bins = histogram(im.flatten(), nbr_bins, density=True)
    cdf = imhist.cumsum()
    cdf = 255.0 * cdf / cdf[-1]
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

pil_im = Image.open('../../img/histeq/ae86.png') #打开原图
pil_im_gray = pil_im.convert('L') #转化为灰度图像
# pil_im_gray.show() #显示灰度图像
# pil_im_gray.save('./img/histeq/gray img.png')
print(pil_im_gray)

im = array(pil_im_gray) #将图片转化为数组的形式
# figure()
# hist(im.flatten(), 256)
# show()

im2, cdf = histeq(im)
# figure()
# hist(im2.flatten(), 256)
# show()

im2 = Image.fromarray(uint8(im2))
# im2.show()
# plot(cdf)
# show()
im2.save('../../img/histeq/equalized img.png')


