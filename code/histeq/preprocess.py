pil_im = Image.open('./img/histeq/ae86.png') #打开原图
pil_im_gray = pil_im.convert('L') #转化为灰度图像
im = array(pil_im_gray) #将图片转化为数组的形式