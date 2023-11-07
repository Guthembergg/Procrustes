import numpy as np
from scipy.spatial import procrustes
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

a = np.array( [[1, 3], [1, 2], [1, 1], [2, 1]])
b = np.array( [[4, -2], [4, -4], [4, -6], [2, -6]])
mtx1, mtx2, disparity = procrustes(a, b)
round(disparity)

#print(mtx1)
"""


a.append(a[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*a) #create lists of x and y values

plt.figure()
plt.plot(xs,ys) 

b.append(b[0]) #repeat the first point to create a 'closed loop'

xs1, ys1 = zip(*b) #create lists of x and y values

plt.figure()
plt.plot(xs1,ys1) 

 #repeat the first point to create a 'closed loop'

xs2, ys2 = zip(*mtx2) #create lists of x and y values

plt.figure()
plt.plot(xs2,ys2) 
print(mtx1)
plt.show()
"""

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