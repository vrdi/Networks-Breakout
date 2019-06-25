# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:19:37 2019

@author: daryl
"""


import networkx as nx
from random import randint, random, choice
import matplotlib.pyplot as plt
from new_seeds_recursive import *


n = 20#grid size
m = 20#grid size
k = 10# number of colors


grid = nx.grid_graph([n,m])

for n in grid.nodes():
    grid.node[n]["population"]=1


def recursive_bi_part(graph, parts, pop_col, epsilon,node_repeats=20,):
    newlabels={}
    pop_target=0
    for node in graph.nodes():
        pop_target+=graph.nodes[node][pop_col]
    pop_target=pop_target/parts
    
    remaining_nodes=list(graph.nodes())
    for n in newlabels.keys():
        remaining_nodes.remove(n)
    sgraph=nx.subgraph(graph,remaining_nodes)
    
    for i in range(parts-1):
        #update=tree_part2(sgraph, pop_col, pop_target, epsilon,node_repeats)#should be part2
        #update = minflow_part(sgraph, pop_col, pop_target, epsilon)
        #update = minflow_part1(sgraph, pop_col, pop_target, epsilon)
        #update =  edge_removal_part(sgraph, pop_col, pop_target, epsilon)#inefficient
        update = part2path2(sgraph, pop_col, pop_target, epsilon)
        #update = part2path3(sgraph, pop_col, pop_target, epsilon)
        #update = part2path(sgraph, pop_col, pop_target, epsilon)
        #update = part2snake(sgraph, pop_col, pop_target, epsilon)
        #update = part2blob(sgraph, pop_col, pop_target, epsilon)
        #update = hier_part(sgraph, pop_col, pop_target, epsilon)
        for x in list(update[1]):
            newlabels[x]=i
        #update pop_target?
        remaining_nodes=list(graph.nodes())
        for n in newlabels.keys():
            remaining_nodes.remove(n)
        
        sgraph=nx.subgraph(graph,remaining_nodes)
        #print("Built District #", i)
        
    td=set(newlabels.keys())
    for nh in graph.nodes():
        if nh not in td:
            newlabels[nh]=parts-1#was +1 for initial testing
    return newlabels


cdict=recursive_bi_part(grid,k,"population",.02,1)


plt.figure()
nx.draw(grid,pos= {x:x for x in grid.nodes()},node_color=[cdict[x] for x in grid.nodes()],node_size=600,cmap='tab20',node_shape='s')#cmap=plt.cm.jet,label=True)
