# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:17:26 2018

@author: daryl
"""
import random
import networkx as nx
import geopandas as gp
from networkx.algorithms import tree
import itertools

import matplotlib.pyplot as plt



def hier_part(graph, pop_col, pop_target, epsilon):

    
    
    h=graph.copy()
    
    clusters = {x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    #removed=[]
    while len(clusters)>2:
        
        chosen_e = random.choice(list(h.edges()))
        ##print(chosen_e)
        
        cpop = clusters[chosen_e[0]][1] + clusters[chosen_e[1]][1]
        #print(cpop)
        

        
        
        if cpop < pop_target + epsilon*pop_target:
            k=h.copy()
            k.remove_node(chosen_e[1])
            if nx.is_connected(k):
                if abs(cpop-pop_target) < epsilon*pop_target:
                    rc=dict()
            
                    rc[1]=clusters[chosen_e[0]][0].union(clusters[chosen_e[1]][0])
                    return rc
                ##print(True,True)
                ##print(clusters[chosen_e[0]])
                ##print(clusters[chosen_e[1]])

            
            
                clusters[chosen_e[0]][1] = cpop
                clusters[chosen_e[0]][0]=clusters[chosen_e[0]][0].union(clusters[chosen_e[1]][0])
                clusters.pop(chosen_e[1])
                #removed.append(chosen_e[1])
                
                h = nx.contracted_edge(h,chosen_e,self_loops = False)
            else:
                ##print(True,False)
                cc=list(nx.connected_components(k))
                tsums=[]
                for l in cc:
                    tsums.append(0)
                    for n in l:
                        ##print(removed)
                        tsums[-1]=tsums[-1]+clusters[n][1]
                
                val, idx = min((val, idx) for (idx, val) in enumerate(tsums))
                
                l=cc[idx]
                    
                for n in l:
                    ##print(n)
                    clusters[chosen_e[1]][1]=clusters[chosen_e[1]][1] + clusters[n][1]
                    clusters[chosen_e[1]][0]=clusters[chosen_e[1]][0].union(clusters[n][0])
                    clusters.pop(n)
                    h.add_edge(chosen_e[1],n)
                    h = nx.contracted_edge(h,(chosen_e[1],n),self_loops = False)
        #else:
            ##print(False)              
        ##print(len(clusters))
    ##print(clusters)
    clusters[1]=clusters[chosen_e[0]][0]
    return clusters


def part2blob(graph, pop_col, pop_target, epsilon):
    

    h=graph.copy()
    
    start = random.choice(list(h.nodes()))
    clusters={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
    neighbors = list(h.neighbors(start))

    while clusters[start][1] < pop_target - epsilon*pop_target:
        
        #print(clusters[start][1]/pop_target)
        
        if neighbors==[]:
            neighbors=list(h.neighbors(start))
            
        for neighbor in neighbors:

    
            
            cpop = clusters[start][1] + clusters[neighbor][1]
            
            if  cpop < pop_target + epsilon*pop_target:
                k=h.copy()
                k.remove_node(start)
                k.remove_node(neighbor)
                #print(len(k.nodes()))
                if nx.is_connected(k):
                    #print(True,True)
                    h = nx.contracted_edge(h,(start,neighbor),self_loops = False)
                    clusters[start][0] = clusters[start][0].union(clusters[neighbor][0])
                    clusters[start][1] = cpop
                    clusters.pop(neighbor)
                else:
                    #print(True,False)
                
                    cc=list(nx.connected_components(k))
                    tsums=[]
                    for l in cc:
                        tsums.append(0)
                        for n in l:
                            ##print(removed)
                            tsums[-1]=tsums[-1]+graph.nodes[n][pop_col]
                    
                    val, idx = min((val, idx) for (idx, val) in enumerate(tsums))
                    
                    l=cc[idx]
                        
                    for n in l:
                        ##print(n)
                        h.add_edge(neighbor,n)
                        #h.nodes[neighbor][pop_col]+=h.nodes[n][pop_col]
                        clusters[neighbor][1] = clusters[neighbor][1]+ clusters[n][1]
                        h = nx.contracted_edge(h,(neighbor,n),self_loops = False)
                        clusters[neighbor][0]=clusters[neighbor][0].union(clusters[n][0])
                        clusters.pop(n)
                        if n in neighbors:
                            neighbors.remove(n)
                        
            else:
                #print(False,False)
                h.remove_edge(start,neighbor)
            neighbors.remove(neighbor)
                

    
    cd2={}
    cd2[start]=clusters[start][0] 
    cd2[-1]=[]
    for node in graph.nodes():
        if node not in cd2[start]:
            cd2[-1].append(node)    
            
    cd2[-1]=set(cd2[-1])
    cs=dict()
    cs[1]=cd2[start]
    #print(cs)
    #print(cs[1])
    return cs


    
    


def part2snake(graph, pop_col, pop_target, epsilon):
    

    h=graph.copy()
    
    start = random.choice(list(h.nodes()))
    clusters={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
    
    while clusters[start][1] < pop_target - epsilon*pop_target:
        
        #print(clusters[start][1]/pop_target)

        if len(list(h.neighbors(start))) > 0:
            neighbor = random.choice(list(h.neighbors(start)))
            
            cpop = clusters[start][1] + clusters[neighbor][1]
            
            if  cpop < pop_target + epsilon*pop_target:
                k=h.copy()
                k.remove_node(start)
                k.remove_node(neighbor)
                #print(len(k.nodes()))
                if nx.is_connected(k):
                    #print(True,True)
                    h = nx.contracted_edge(h,(start,neighbor),self_loops = False)
                    clusters[start][0] = clusters[start][0].union(clusters[neighbor][0])
                    clusters[start][1] = cpop
                    clusters.pop(neighbor)
                else:
                    #print(True,False)
                
                    cc=list(nx.connected_components(k))
                    tsums=[]
                    for l in cc:
                        tsums.append(0)
                        for n in l:
                            ##print(removed)
                            tsums[-1]=tsums[-1]+graph.nodes[n][pop_col]
                    
                    val, idx = min((val, idx) for (idx, val) in enumerate(tsums))
                    
                    l=cc[idx]
                        
                    for n in l:
                        ##print(n)
                        h.add_edge(neighbor,n)
                        #h.nodes[neighbor][pop_col]+=h.nodes[n][pop_col]
                        clusters[neighbor][1] = clusters[neighbor][1]+ clusters[n][1]
                        h = nx.contracted_edge(h,(neighbor,n),self_loops = False)
                        clusters[neighbor][0]=clusters[neighbor][0].union(clusters[n][0])
                        clusters.pop(n)
                        
            else:
                #print(False,False)
                h.remove_edge(start,neighbor)
                
                
            

    
    cd2=dict()
    #cd2[start]=clusters[start][0] 
    #cd2[-1]=[]
    #for node in graph.nodes():
    #    if node not in cd2[start]:
    #        cd2[-1].append(node)    
            
    #cd2[-1]=set(cd2[-1])
    cd2[1]=clusters[start][0]
    return cd2
                
                
def part2path(graph, pop_col, pop_target, epsilon):
    

    h=graph.copy()
    
    start = random.choice(list(h.nodes()))
    clusters={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
    
    while clusters[start][1] < pop_target - epsilon*pop_target:
        
        #print(clusters[start][1]/pop_target)

        
        end = start
        while end == start:
            end = random.choice(list(h.nodes()))
            
        path = nx.shortest_path(h,source=start,target=end)
    
        psum = 0
        for p in path:
            psum += clusters[p][1]

        if psum < pop_target + epsilon*pop_target:
            #print(True)
             
            cpop = psum
            
            if  cpop < pop_target + epsilon*pop_target:
                k=h.copy()
                k.remove_nodes_from(path)

                #print(len(k.nodes()))
                if nx.is_connected(k):
                    path.remove(start)
                    #print(True,True)
                    for p in path:
                        h.add_edge(start,p)
                        h = nx.contracted_edge(h,(start,p),self_loops = False)
                        clusters[start][0] = clusters[start][0].union(clusters[p][0])
                        clusters[start][1] = cpop
                        clusters.pop(p)
                #else:
                    #print(True,False)
                
                        
            #else:
           #     #print(False,False)
            #    h.remove_edge(start,neighbor)
            

    
    cd2={}
    cd2[start]=clusters[start][0] 
    cd2[-1]=[]
    for node in graph.nodes():
        if node not in cd2[start]:
            cd2[-1].append(node)    
            
    cd2[-1]=set(cd2[-1])
    return cd2
                

def part2path3(graph, pop_col, pop_target, epsilon):
    

    h=graph.copy()
    
    start = random.choice(list(h.nodes()))
    clusters={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
    
    while clusters[start][1] < pop_target - epsilon*pop_target:
        
        #print(clusters[start][1]/pop_target)

        
        end = start
        while end == start:
            end = random.choice(list(h.nodes()))
            
        path = nx.shortest_path(graph,source=start,target=end)
    
        psum = 0
        for p in path:
            if p not in clusters[start][0]:
                psum += clusters[p][1]

        if psum + clusters[start][0] < pop_target + epsilon*pop_target:
            #print(True)
             
            cpop = psum
            
            if  cpop < pop_target + epsilon*pop_target:
                k=h.copy()
                k.remove_nodes_from(path)

                #print(len(k.nodes()))
                if nx.is_connected(k):
                    path.remove(start)
                    #print(True,True)
                    for p in path:
                        h.add_edge(start,p)
                        h = nx.contracted_edge(h,(start,p),self_loops = False)
                        if p not in clusters[start][0]:
                            clusters[start][0] = clusters[start][0].union(clusters[p][0])
                            clusters[start][1] += clusters[p][1]
                        #clusters.pop(p)
                #else:
                    #print(True,False)
                
                        
            #else:
           #     #print(False,False)
            #    h.remove_edge(start,neighbor)
            

    
    cd2=dict()
    #cd2[start]=clusters[start][0] 
    #cd2[-1]=[]
    #for node in graph.nodes():
    #    if node not in cd2[start]:
    #        cd2[-1].append(node)    
    #        
    #cd2[-1]=set(cd2[-1])
    
    cd2[1]=clusters[start][0]

    return cd2
                
                
def part2path2(graph, pop_col, pop_target, epsilon):
    

    h=graph.copy()
    
    start = random.choice(list(h.nodes()))
    clusters={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
    
    while clusters[start][1] < pop_target - epsilon*pop_target:
        
        #print(clusters[start][1]/pop_target)

        
        end = start
        while end == start:
            end = random.choice(list(h.nodes()))
            
        path = nx.shortest_path(graph,source=start,target=end)
    
        psum = 0
        for p in path:
            psum += clusters[p][1]

        if psum < pop_target + epsilon*pop_target:
            #print(True)
             
            cpop = psum
            
            if  cpop < pop_target + epsilon*pop_target:
                k=h.copy()
                k.remove_nodes_from(path)

                #print(len(k.nodes()))
                if nx.is_connected(k):
                    path.remove(start)
                    #print(True,True)
                    for p in path:
                        h.add_edge(start,p)
                        h = nx.contracted_edge(h,(start,p),self_loops = False)
                        if p not in clusters[start][0]:
                            clusters[start][0] = clusters[start][0].union(clusters[p][0])
                            clusters[start][1] += clusters[p][1]
                        #clusters.pop(p)
                #else:
                    #print(True,False)
                
                        
            #else:
           #     #print(False,False)
            #    h.remove_edge(start,neighbor)
            

    
    cd2={}
    cd2[start]=clusters[start][0] 
    cd2[-1]=[]
    for node in graph.nodes():
        if node not in cd2[start]:
            cd2[-1].append(node)    
            
    cd2[-1]=set(cd2[-1])
    
    cs=dict()
    cs[1]=cd2[start]
    #print(cs)
    #print(cs[1])
    return cs
                
                
def tree_part(graph, pop_col, pop_target, epsilon,node_repeats):
    
    w=graph.copy()
    for ed in w.edges():
        w.add_edge(ed[0],ed[1],weight=random.random())
    
    T = tree.maximum_spanning_edges(w, algorithm='kruskal', data=False)
    ST= nx.Graph()
    ST.add_edges_from(list(T))
    #nx.draw(ST)
    h=ST.copy()
    for e in ST.edges():
        ##print(e)
        #e=random.choice(list(ST.edges()))#new

        h.remove_edge(e[0],e[1])
        for t in nx.connected_components(h):
            
            tsum=0
            for n in t:
                tsum+=graph.nodes[n][pop_col]
            
            #print(tsum/pop_target)
            if abs(tsum-pop_target) < pop_target * epsilon:
                ##print("MADE IT")
                clusters={}
                clusters[1]=list(t)
                clusters[-1]=[]
                for nh in graph.nodes():
                    if nh not in clusters[1]:
                        clusters[-1].append(nh)
                        
                
                    
                return clusters
        h.add_edge(e[0],e[1])

def tree_part2(graph, pop_col, pop_target, epsilon,node_repeats):
    
    w=graph.copy()
    for ed in w.edges():
        w.add_edge(ed[0],ed[1],weight=random.random())
    
    T = tree.maximum_spanning_edges(w, algorithm='kruskal', data=False)
    ST= nx.Graph()
    ST.add_edges_from(list(T))
    #nx.draw(ST)
    h=ST.copy()
    
    #nx.draw(ST,layout='tree')
    
    #root = random.choice(list(h.nodes()))
    root = random.choice([x for x in ST.nodes() if ST.degree(x)>1])#this used to be greater than 2 but failed on small grids:(
    ##print(root)
    predbfs=nx.bfs_predecessors(h, root)#was dfs
    pred={}
    for ed in predbfs:
        pred[ed[0]]=ed[1]

    pops={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
    leaves=[]
    t=0
    layer=0
    restarts=0
    while 1==1:
        if restarts==node_repeats:
        
        
            w=graph.copy()
            for ed in w.edges():
                w.add_edge(ed[0],ed[1],weight=random.random())
    
            T = tree.maximum_spanning_edges(w, algorithm='kruskal', data=False)
            ST= nx.Graph()
            ST.add_edges_from(list(T))
            #nx.draw(ST)
            h=ST.copy()
    
        #nx.draw(ST,layout='tree')
    
            #root = random.choice(list(h.nodes()))
            root = random.choice([x for x in ST.nodes() if ST.degree(x)>1])#this used to be greater than 2 but failed on small grids:(
            ##print(root)
            predbfs=nx.bfs_predecessors(h, root)#was dfs
            pred={}
            for ed in predbfs:
                pred[ed[0]]=ed[1]

            pops={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
    
            leaves=[]
            t=0
            layer=0
            restarts=0
            ##print("Bad tree -- rebuilding")
            
        if len(list(h.nodes()))==1:
            h=ST.copy()
            root = random.choice([x for x in ST.nodes() if ST.degree(x)>1])#this used to be greater than 2 but failed on small grids:(
            ##print(root)
            #pred=nx.bfs_predecessors(h, root)#was dfs
            predbfs=nx.bfs_predecessors(h, root)#was dfs
            pred={}
            for ed in predbfs:
                pred[ed[0]]=ed[1]
            pops={x:[{x},graph.nodes[x][pop_col]] for x in graph.nodes()}
            ##print("bad root --- restarting",restarts)
            restarts+=1
            layer=0
            leaves=[]
            
        if leaves == []:
        
            leaves = [x for x in h.nodes() if h.degree(x)==1]
            layer=layer+1
            
            if len(leaves) == len(list(h.nodes()))-1:
                tsum = pops[root][1]
                for r in range(2,len(leaves)):
                    for s in itertools.combinations(leaves,r):
                        for node in s:
                            tsum+=pops[node][1]
                    if abs(tsum-pop_target)<epsilon*pop_target:
                        #print(pops[leaf][1]/pop_target)
                        clusters={}
                        clusters[1]=list(pops[leaf][0])
                        clusters[-1]=[]
                        for nh in graph.nodes():
                            if nh not in clusters[1]:
                                clusters[-1].append(nh)
                        return clusters

            if root in leaves: #this was in an else before but is still apparently necessary?
                    leaves.remove(root)
                
            #if layer %10==0:
                ##print("Layer",layer)
                
            

            
        for leaf in leaves:
            if layer>1 and abs(pops[leaf][1]-pop_target) < pop_target * epsilon:
                ##print(pops[leaf][1]/pop_target)
                #ST.remove_edge(leaf,pred[leaf])#One option but slow
                #parts=list(nx.connected_components(h)) #ST here too
                ##print(layer, len(parts))

                #part=parts[random.random()<.5]
                clusters={}
                clusters[1]=list(pops[leaf][0])
                clusters[-1]=[]
                for nh in graph.nodes():
                    if nh not in clusters[1]:
                        clusters[-1].append(nh)
                return clusters

            parent = pred[leaf]
            
            pops[parent][1]+=pops[leaf][1]
            pops[parent][0]=pops[parent][0].union(pops[leaf][0])
            #h = nx.contracted_edge(h,(parent,leaf),self_loops = False)#too slow on big graphs
            h.remove_node(leaf)
            leaves.remove(leaf)
            t=t+1
            #if t%1000==0:
            #    #print(t)
         
            
def recursive_tree_part(graph, parts, pop_col, epsilon,node_repeats=20,):
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
        update=tree_part2(sgraph, pop_col, pop_target, epsilon,node_repeats)#should be part2
    
        for x in list(update[1]):
            newlabels[x]=i
        #update pop_target?
        remaining_nodes=list(graph.nodes())
        for n in newlabels.keys():
            remaining_nodes.remove(n)
        
        sgraph=nx.subgraph(graph,remaining_nodes)
        ##print("Built District #", i)
        
    td=set(newlabels.keys())
    for nh in graph.nodes():
        if nh not in td:
            newlabels[nh]=parts-1#was +1 for initial testing
    return newlabels
        
def minflow_part1(graph, pop_col, pop_target, epsilon):#doesn't work yet
    
    
    while 1==1:
        
        w=graph.copy()
        for ed in w.edges():
            w.add_edge(ed[0],ed[1],capacity=random.random())
            
            
        
        start = random.choice(list(w.nodes()))
        end = random.choice(list(w.nodes()))
        ##print(len(list(graph.neighbors(start))))
        ##print(len(list(graph.neighbors(end))))
        for n in list(graph.neighbors(start)):
            w.add_edge(start,n,capacity=100)
            for k in list(graph.neighbors(n)):
                w.add_edge(n,k,capacity=100)
                for j in list(graph.neighbors(k)):
                    w.add_edge(j,k,capacity=100)
                    for l in list(graph.neighbors(j)):
                        w.add_edge(j,l,capacity=100)
                        for f in list(graph.neighbors(l)):
                            w.add_edge(f,l,capacity=100)
                            for g in list(graph.neighbors(f)):
                                w.add_edge(f,g,capacity=100)
                    
        for n in list(graph.neighbors(end)):
            w.add_edge(end,n,capacity=100)
            for k in list(graph.neighbors(n)):
                w.add_edge(n,k,capacity=100)
                for j in list(graph.neighbors(k)):
                    w.add_edge(j,k,capacity=100)
                    for l in list(graph.neighbors(j)):
                        w.add_edge(j,l,capacity=100)
                        for f in list(graph.neighbors(l)):
                            w.add_edge(f,l,capacity=100)
                            for g in list(graph.neighbors(f)):
                                w.add_edge(f,g,capacity=100)
                
        
                
            
        

            

        val,P = nx.minimum_cut(w, start,end,capacity='capacity')
        path = list(nx.shortest_path(graph,source=start,target=end))

        clusters={}
        clusters[1]=P[0]
        clusters[-1]=P[1]
        clusters[2] = [start]
        clusters[3] =[end]     
        path.remove(start)
        path.remove(end)
        clusters[4]=path
        tsum =0
        for n in P[0]:
            tsum+=graph.nodes[n][pop_col]
        #print(tsum/pop_target)
        if abs(tsum-pop_target) < epsilon*pop_target:
            return clusters
               
def minflow_part(graph, pop_col, pop_target, epsilon):
    
    
    while 1==1:
        
        w=graph.copy()
        for ed in w.edges():
            w.add_edge(ed[0],ed[1],capacity=random.random())
            
            
        
        start = random.choice(list(w.nodes()))
        
        elist = list(w.nodes())
        elist.remove(start)
        end = random.choice(elist)
        ##print(len(list(graph.neighbors(start))))
        ##print(len(list(graph.neighbors(end))))
        pstart= nx.shortest_path_length(graph,source=start)
        pend=nx.shortest_path_length(graph,source=end)
        
        for ed in graph.edges():
            wt=-4
            dmax=max(pstart[ed[0]],pstart[ed[1]],pend[ed[0]],pend[ed[1]])
            dmin=min(pstart[ed[0]],pstart[ed[1]],pend[ed[0]],pend[ed[1]])
            wt = 10**(-(dmin-3)+random.random()) 
            w.add_edge(ed[0],ed[1],capacity=random.gauss(wt,wt/100))
        
                
            
        

            

        val,P = nx.minimum_cut(w, start,end,capacity='capacity')
        
        
        path = list(nx.shortest_path(graph,source=start,target=end))

        clusters={}
        clusters[1]=P[0]
        clusters[-1]=P[1]
        clusters[2] = [start]
        clusters[3] =[end]     
        path.remove(start)
        path.remove(end)
        clusters[4]=path
        tsum =0
        for n in P[0]:
            tsum+=graph.nodes[n][pop_col]
        #print(tsum/pop_target)
        if abs(tsum-pop_target) < epsilon*pop_target:
            return clusters
        
        
def edge_removal_part(graph, pop_col, pop_target, epsilon):
    
    w=graph.copy()
    wlist=[x for x in range(10)]
    temp=0
    while 1==1:
        e = random.choice(list(w.edges()))
        w.remove_edge(e[0],e[1])
        
        if not nx.is_connected(w):
            cc=list(nx.connected_components(w))
            tsums=[]
            for l in cc:
                tsums.append(0)
                for n in l:
                    ##print(removed)
                    tsums[-1]=tsums[-1]+graph.nodes[n][pop_col]
            
            val, idx = min((val, idx) for (idx, val) in enumerate(tsums))
            #print(len(list(w.edges())),val/pop_target)
            wlist[temp]=len(list(w.edges()))
            temp+=1
            temp=temp%10
            if abs(val -pop_target) < epsilon*pop_target:
                l=cc[idx]
                clusters={}
                clusters[1]=list(l)
                clusters[-1]=[]

                for n in graph.nodes():
                    if n not in l:
                        clusters[-1].append(n)
                return clusters
            else:
                w.add_edge(e[0],e[1])
                if len(set(wlist))==1:
                    w=graph.copy()
            

                

            
            
        
                               


            
        


    
    
    
    
    
    
    
    