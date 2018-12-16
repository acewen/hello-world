import numpy as np
from random import uniform

# variable x and y
rawdata = np.genfromtxt('sample_data.csv', delimiter=',')
x = rawdata[1:,:3]
y = rawdata[1:,3]
print(x.shape, y.shape)


x2 = np.matmul(x.T, x)
w = np.ones((3,1))
print(x2.shape, w.shape)

a = 0.00000001

i = 1
while i < 1000000:
    i = i + 1
    w = w - a*(np.matmul(x2,w)- np.matmul(x.T,y))
print(w)

#for verification
#xx = np.linalg.inv(x2)
#xy = np.matmul(x.T,y)
#print(np.matmul(xx,xy))
