img = cv2.imread('../../img/laplace/f1.png') #读入图像
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #将图像转化为灰度格式
cv2.imwrite('../../img/laplace/grey.png', img) #存储灰度图像

laplace = np.array([[0,1,0],[1,-4,1],[0,1,0]]) #定义卷积核
img = imgEnhancement(img, laplace) #进行拉普拉斯图像增强
cv2.imwrite('../../img/laplace/enhanced img1.png', img) #存储增强图像
