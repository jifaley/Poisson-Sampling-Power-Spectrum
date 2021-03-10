import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import random


def Random_sampling(width = 1.0, height = 1.0, n = 1024):
    points = np.zeros([n,2])
    for i in range(n):
        points[i][0] = random.random()
        points[i][1] = random.random()
    return points
    

matplotlib.rcParams['toolbar'] = 'None'
points = Random_sampling()
print("Random_sampling,", len(points), "points in total")

'''

fig = plt.figure(figsize=(1, 1), dpi=256, facecolor='white')
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)


X = [x for (x, y) in points]
Y = [y for (x, y) in points]
#ax.scatter(X, Y, s=5, lw=0.5, edgecolor='k', facecolor="None")
ax.scatter(X, Y, s=0.1, color='k')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('Random.jpg')
'''

a_arr = np.ones([256,256],dtype=np.uint8)*255
for (x,y) in points:
    a_arr[int(x*255),int(y*255)] = 0

plt.imshow(a_arr,cmap=plt.cm.gray)
matplotlib.image.imsave('Random.jpg', a_arr,cmap=plt.cm.gray)


plt.show()
