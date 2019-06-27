# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:50:03 2019

@author: daryl
"""

import networkx as nx

g = nx.grid_graph([10,10])

initial_infection = 4
recover = .2
spread = .1
reinfect = False

S={n for n in graph.nodes()}
I={}
R={}

Ss=[len(graph.nodes())]
Is=[]
Rs=[0]


num_steps = 100

nx.draw()








