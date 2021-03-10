import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def Bridson_sampling(width=1.0, height=1.0, radius=0.025, k=30):

    # 计算两点之间距离的平方
    def squared_distance(p0, p1):
        return (p0[0]-p1[0])**2 + (p0[1]-p1[1])**2

    # 生成某一点周围一定半径范围内“均匀分布”的随机点，虽然不是真随机，但忍了
    def random_point_around(p, k=1):
        R = np.random.uniform(radius, 2*radius, k)  # 距离
        T = np.random.uniform(0, 2*np.pi, k)  # 角度
        P = np.empty((k, 2))  # 目标点位置矩阵
        P[:, 0] = p[0]+R*np.sin(T)
        P[:, 1] = p[1]+R*np.cos(T)
        return P

    # 判断是否处于给定范围内
    def in_limits(p):
        return 0 <= p[0] < width and 0 <= p[1] < height

    # 返回某个坐标周围n格范围内的坐标
    def neighborhood(shape, index, n=2):
        row, col = index
        row0, row1 = max(row-n, 0), min(row+n+1, shape[0])
        col0, col1 = max(col-n, 0), min(col+n+1, shape[1])
        I = np.dstack(np.mgrid[row0:row1, col0:col1])
        I = I.reshape(I.size//2, 2).tolist()
        I.remove([row, col])
        return I

    def in_neighborhood(p):
        i, j = int(p[0]/cellsize), int(p[1]/cellsize)
        if M[i, j]:
            return True
        for (i, j) in N[(i, j)]:
            if M[i, j] and squared_distance(p, P[i, j]) < squared_radius:
                return True
        return False

    def add_point(p):
        points.append(p)
        i, j = int(p[0]/cellsize), int(p[1]/cellsize)
        P[i, j], M[i, j] = p, True

    # 2 对应空间维数，此时考虑平面，故为2
    cellsize = radius/np.sqrt(2)  # 划分网格的边长
    rows = int(np.ceil(width/cellsize))  # 网格行数
    cols = int(np.ceil(height/cellsize))  # 网格列数

    squared_radius = radius*radius

    P = np.zeros((rows, cols, 2), dtype=np.float32)  # 用于存储网格内的点
    M = np.zeros((rows, cols), dtype=bool)  # 用于存储mask

    # Cache generation for neighborhood
    N = {}
    for i in range(rows):
        for j in range(cols):
            N[(i, j)] = neighborhood(M.shape, (i, j), 2)

    points = []
    add_point((np.random.uniform(width), np.random.uniform(height)))
    while len(points):
        #         print(len(points))
        i = np.random.randint(len(points))
        p = points[i]

        Q = random_point_around(p, k)
        success_in_k_trial = False
        for q in Q:
            if in_limits(q) and not in_neighborhood(q):
                add_point(q)
        if not success_in_k_trial:
            del points[i]
    return P[M]

matplotlib.rcParams['toolbar'] = 'None'
points = Bridson_sampling()
print("Bridson_sampling,", len(points), "points in total")

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

plt.savefig('Bridson.jpg')

'''
a_arr = np.ones([256,256],dtype=np.uint8)*255
for (x,y) in points:
    a_arr[int(x*255),int(y*255)] = 0

plt.imshow(a_arr,cmap=plt.cm.gray)
matplotlib.image.imsave('Bridson.jpg', a_arr,cmap=plt.cm.gray)



plt.show()
