#16/03/2016

#packages: Numpy / scipy / matplotlib

#from scipy.misc import imread,imsave,imresize
import matplotlib.pyplot as plt
import numpy as np

#img = imread("/Users/alonshmilovich/Downloads/logo.png")

#print(img.dtype, img.shape)

#img2 = img *[1,0,0]

#imsave("/Users/alonshmilovich/Downloads/logo2.png", img2)

#print(img2.dtype, img2.shape)

#plt.imshow(img2)
#plt.show()

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)

y1 = np.cos(x)
plt.plot(x,y1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('title')

plt.legend(['sin','cos'])
plt.show()

#spliting to 2 windows
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.plot(x,y)

