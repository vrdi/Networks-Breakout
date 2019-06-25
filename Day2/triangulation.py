import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
import networkx as nx

a = 1 
b = 1
num_points = 20

points = np.random.rand(num_points, 2)
points[:, 0] = a*points[:, 0] 
points[:, 1] = b*points[:, 1] 

tri = Delaunay(points)


plt.triplot(points[:, 0], points[:, 1], tri.simplices.copy())
plt.triplot(points[:, 0], points[:, 1], 'o')
plt.show()

nlist = tri.vertex_neighbor_vertices

g = nx.Graph()

for n in range(num_points):
    g.add_edges_from([(n,x) for x in nlist[1][nlist[0][n]:nlist[0][n+1]]])
    
pos = { n : points[n, :] for n in range(num_points)}

nx.draw(g,pos=pos)
plt.show()
