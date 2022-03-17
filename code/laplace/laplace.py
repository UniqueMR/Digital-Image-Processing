def imgEnhancement(img, laplace):
    """使用Laplace算子进行图像增强"""
    """
    parameters:
           img: 待增强图像
           laplace: 拉普拉斯卷积核
    """
    row, col = img.shape #提取图像的行数和列数
    new_img = np.zeros((row, col)) #根据原图的行数和列数，创建新图像容器

    #使用卷积核进行离散域拉普拉斯运算
    for i in range(row - 2):
        for j in range(col - 2):
            # 以下两个表达式分别用于图像增强(1)和得到拉普拉斯图像(2)
            new_img[i+1, j+1] = abs(np.sum(img[i:i+3,j:j+3] * laplace))\
            + img[i+1,j+1] #1
            new_img[i+1, j+1] = abs(np.sum(img[i:i+3,j:j+3] * laplace)) #2

    return np.uint8(new_img) #返回新图像    