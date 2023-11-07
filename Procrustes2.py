import numpy as np
from scipy.linalg import orthogonal_procrustes
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
from math import sin, cos


a = np.array( [[1, 3], [1, 2], [1, 1], [2, 1],[8,5]])
b = np.array( [[4, -2], [4, -4], [4, -6], [2, -6],[2, 1]])



def procrustes(data1, data2):
    mtx1 = np.array(data1, dtype=np.double, copy=True)
    mtx2 = np.array(data2, dtype=np.double, copy=True)

    if mtx1.ndim != 2 or mtx2.ndim != 2:
        raise ValueError("Input matrices must be two-dimensional")
    if mtx1.shape != mtx2.shape:
        raise ValueError("Input matrices must be of same shape")
    if mtx1.size == 0:
        raise ValueError("Input matrices must be >0 rows and >0 cols")

    # translate all the data to the origin
    mtx1 -= np.mean(mtx1, 0)
    mtx2 -= np.mean(mtx2, 0)

    norm1 = np.linalg.norm(mtx1)
    norm2 = np.linalg.norm(mtx2)

    if norm1 == 0 or norm2 == 0:
        raise ValueError("Input matrices must contain >1 unique points")

    # change scaling of data (in rows) such that trace(mtx*mtx') = 1
    mtx1 /= norm1
    mtx2 /= norm2

    # transform mtx2 to minimize disparity
    R, s = orthogonal_procrustes(mtx1, mtx2)
    mtx2 = np.dot(mtx2, R.T) * s    # HERE, the projected mtx2 is estimated.

    # measure the dissimilarity between the two datasets
    disparity = np.sum(np.square(mtx1 - mtx2))

    return mtx1, mtx2, disparity, R,s


mtx1,mtx2,disp,R ,s= procrustes(a,b)
print(R)
p = Polygon(a, facecolor = 'g',)
p1=Polygon(b, facecolor = 'k')
p2= Polygon(mtx1, facecolor = 'b')
fig,ax = plt.subplots()

ax.add_patch(p)
ax.add_patch(p1)
ax.add_patch(p2)

ax.set_xlim([-7,7])
ax.set_ylim([-7,7])
plt.show()






