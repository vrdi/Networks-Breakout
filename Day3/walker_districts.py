# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 07:56:10 2019

@author: daryl
"""

import networkx as nx
from random import randint, random, choice, shuffle
import matplotlib.pyplot as plt
import numpy as np

n = 20#grid size
m = 20#grid size
k = 20# number of walkers
ns = 500

grid = nx.grid_graph([n,m])
 
unassigned = list(grid.nodes())

walkers=[]

cdict={x:0 for x in grid.nodes()}


for i in range(k):
    walkers.append(choice(unassigned))
    unassigned.remove(walkers[-1])
    cdict[walkers[-1]]=i+1
    
plt.figure()

nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=ns,cmap='tab20',node_shape='s')#cmap=plt.cm.jet,label=True)
plt.title("Initial Walkers")
plt.show()

move = 0

while unassigned:
    order = list(range(k))
    shuffle(order)
	
    for i in order:
        old=walkers[i]
        #print(old)
        walkers[i]=choice(list(grid.neighbors(walkers[i])))
        #print(walkers[i])
        if walkers[i] in unassigned:
            unassigned.remove(walkers[i])
            cdict[walkers[i]]=i+1
            grid = nx.contracted_nodes(grid, walkers[i], old, self_loops=False)
        else:
            walkers[i]=old
    #plt.figure()
    #nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20')#cmap=plt.cm.jet,label=True)

            
plt.figure()
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=['k' for x in grid.nodes()],node_shape='s',node_size=25)
plt.title("Dual Graph")

plt.show()

grid2 = nx.grid_graph([n,m])
plt.figure()
nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[cdict[x] for x in grid2.nodes()],node_size=ns,cmap='tab20',node_shape='s')#cmap=plt.cm.jet,label=True)
plt.title("Full Partition")

plt.show()



slist = list(range(max(cdict.values())+1))
np.random.shuffle(slist)


reverse_cdict = {x:[[],[]] for x in range(max(cdict.values())+1)}
grid2 = nx.grid_graph([n,m])

for node in grid2.nodes():
    reverse_cdict[cdict[node]][0].append(node[0])
    reverse_cdict[cdict[node]][1].append(node[1])
    
fig = plt.figure()


nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[slist[cdict[x]] for x in grid2.nodes()],cmap=plt.cm.jet,node_shape='s',node_size=ns,kwds = {'zorder':1})    

nx.draw(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},label=True,node_color=['w' for x in grid.nodes()],node_size=25,kwds = {'zorder':100})

#nx.draw_networkx_edges(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},kwds = {'zorder':100},width=10)

for edge in grid.edges():
    plt.plot([np.mean(reverse_cdict[cdict[edge[0]]][0]),np.mean(reverse_cdict[cdict[edge[1]]][0])],[np.mean(reverse_cdict[cdict[edge[0]]][1]),np.mean(reverse_cdict[cdict[edge[1]]][1])],'w')



#fig.set_facecolor("lightpink")
plt.title("Dual Graph")
plt.show()

#print(max(cdict.values()))
#print(slist)
#print(cdict)


"""


corners = nx.Graph()


for rect in rectangles:
    corners.add_node((rect[0][0]-.5,rect[0][1]-.5))
    corners.add_node((rect[1][0]+.5,rect[1][1]+.5))
    corners.add_node((rect[0][0]-.5,rect[1][1]+.5))
    corners.add_node((rect[1][0]+.5,rect[0][1]-.5))
    
    corners.add_edge((rect[0][0]-.5,rect[0][1]-.5),(rect[0][0]-.5,rect[1][1]+.5))
    corners.add_edge((rect[0][0]-.5,rect[0][1]-.5),(rect[1][0]+.5,rect[0][1]-.5))    
    corners.add_edge((rect[1][0]+.5,rect[1][1]+.5),(rect[0][0]-.5,rect[1][1]+.5))
    corners.add_edge((rect[1][0]+.5,rect[1][1]+.5),(rect[1][0]+.5,rect[0][1]-.5))    

plt.figure()

nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[slist[cdict[x]] for x in grid2.nodes()],cmap=plt.cm.jet,node_shape='s',node_size=25)    

nx.draw(corners, pos = {x:x for x in corners.nodes()}, node_color = ['k' for x in corners.nodes()], node_shape='s',node_size=25)

for edge in corners.edges():
    plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],'k')


plt.title("Corners")
plt.show()

fig = plt.figure()

nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[slist[cdict[x]] for x in grid2.nodes()],cmap=plt.cm.jet,node_shape='s',node_size=25)    

nx.draw(corners, pos = {x:x for x in corners.nodes()}, node_color = ['k' for x in corners.nodes()], node_shape='s',node_size=25)


#nx.draw_networkx_edges(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},kwds = {'zorder':100},width=10)

for edge in grid.edges():
    plt.plot([np.mean(reverse_cdict[cdict[edge[0]]][0]),np.mean(reverse_cdict[cdict[edge[1]]][0])],[np.mean(reverse_cdict[cdict[edge[0]]][1]),np.mean(reverse_cdict[cdict[edge[1]]][1])],'w')
    
for edge in corners.edges():
    plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],'k')


nx.draw(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},node_color=['w' for x in grid2.nodes()],node_size=25)

plt.plot([],[],'k',label="Corners")
plt.plot([],[],'w',label="Dual Graph")

fig.set_facecolor("lightpink")
plt.title("Overlays")
plt.legend()
plt.show()


fig = plt.figure()

nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[slist[cdict[x]] for x in grid2.nodes()],cmap=plt.cm.jet,node_shape='s',node_size=ns)    

nx.draw(corners, pos = {x:x for x in corners.nodes()}, node_color = ['k' for x in corners.nodes()], node_shape='s',node_size=25)


#nx.draw_networkx_edges(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},kwds = {'zorder':100},width=10)

for edge in grid.edges():
    plt.plot([np.mean(reverse_cdict[cdict[edge[0]]][0]),np.mean(reverse_cdict[cdict[edge[1]]][0])],[np.mean(reverse_cdict[cdict[edge[0]]][1]),np.mean(reverse_cdict[cdict[edge[1]]][1])],'w')
    
for edge in corners.edges():
    plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],'k')


nx.draw(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},node_color=['w' for x in grid2.nodes()],node_size=25)

plt.plot([],[],'k',label="Corners")
plt.plot([],[],'w',label="Dual Graph")

fig.set_facecolor("lightpink")
plt.title("Overlays")
plt.legend()
plt.show()

if pt:    
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1, adjustable='box', aspect=1)#plt.subplot(1,2,1)
    #nx.draw(grid,pos= {x:x for x in grid.nodes()},label=True,node_shape='s',node_size=50)
    nx.draw(grid,pos= {x:(np.mean(reverse_cdict[cdict[x]][0]),np.mean(reverse_cdict[cdict[x]][1])) for x in grid.nodes()},label=True,node_shape='s',node_color=['k' for x in grid2.nodes()],node_size=50)
    
    grid2 = nx.grid_graph([n,m])
    
    ax2 = fig.add_subplot(1,2,2, adjustable='box', aspect=1)#plt.subplot(1,2,2)
    nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[slist[cdict[x]] for x in grid2.nodes()],cmap='tab20',node_shape='s',node_size=ns)#,plt.cm.jet,label=True)
    plt.show()
else:
    plt.figure()
    nx.draw(grid,pos= {x:x for x in grid.nodes()},label=True,node_shape='s',node_size=100)
    grid2 = nx.grid_graph([n,m])
    plt.show()
    plt.figure()
    nx.draw(grid2,pos= {x:x for x in grid2.nodes()},node_color=[slist[cdict[x]] for x in grid2.nodes()],cmap=plt.cm.jet,node_shape='s',node_size=ns)#,label=True)
    plt.show()
        
"""
	

'''# Alternative for Random Choice of next walker:
order = list(range(k))
while unassigned:
    i = choice(order)
    
    old=walkers[i]
    #print(old)
    walkers[i]=choice(list(grid.neighbors(walkers[i])))
    #print(walkers[i])
    if walkers[i] in unassigned:
        unassigned.remove(walkers[i])
        cdict[walkers[i]]=i+1
        grid = nx.contracted_nodes(grid, walkers[i], old, self_loops=False)
    else:
        walkers[i]=old

'''


