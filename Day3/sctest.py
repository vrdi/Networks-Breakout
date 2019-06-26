import networkx as nx
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn import metrics

G = nx.karate_club_graph()
n=34
G = nx.grid_graph([5,5])
n=25
AM = nx.adjacency_matrix(G)
NLM = (nx.normalized_laplacian_matrix(G)).todense()
LM = (nx.laplacian_matrix(G)).todense()

'''
Labels = [G.nodes[i]['club'] != 'Mr. Hi' for i in G.nodes()]


plt.figure()
plt.title("Data Labels")
nx.draw(G, node_color=Labels )
plt.show()
'''
#scipy.linalg.eigh(NLM,eigvals=1)#replace with this for speed
NLMva, NLMve = LA.eigh(NLM)

LMva, LMve = LA.eigh(LM)

Fv = LMve[:,1]
xFv = [Fv.item(x) for x in range(n)]
NFv = NLMve[:,1]
xNFv = [NFv.item(x) for x in range(n)]

plt.figure()
plt.title("Laplacian Eigenvalues")
nx.draw(G, node_color=xFv )
plt.show()

plt.figure()
plt.title("Normalized Laplacian Eigenvalues")
nx.draw(G,node_color= xNFv)
plt.show()

plt.figure()
plt.title("Binarized Laplacian Eigenvalues")
nx.draw(G, node_color=[xFv[x] > 0 for x in range(n)] )
plt.show()

plt.figure()
plt.title("Binarized Normalized Laplacian Eigenvalues")
nx.draw(G,node_color= [xNFv[x] > 0 for x in range(n)])
plt.show()


sc = SpectralClustering(2, affinity='precomputed', assign_labels='discretize')

sc.fit(AM)

plt.figure()
plt.title("Scikit Spectral Clustering")
nx.draw(G,node_color= sc.labels_)
plt.show()












