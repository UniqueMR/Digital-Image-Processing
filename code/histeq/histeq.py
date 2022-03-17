def histeq(im, nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""
    imhist, bins = histogram(im.flatten(), nbr_bins, density=True)
    cdf = imhist.cumsum()
    cdf = 255.0 * cdf / cdf[-1]
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

    