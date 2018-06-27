import numpy as np
import networkx as nx
from heapq import heappop, heappush
from collections import defaultdict
import matplotlib.pyplot as plt

vertex_pos = {}
edge_weight = []

f = open('Graph.graph', 'r')
spl = f.readline().split('\t')
nv, ne = int(spl[0]), int(spl[1])
for i in range(0, nv):
    spl = f.readline().split('\t')
    vertex_pos[i] = np.array((float(spl[1]), float(spl[0])))

for i in range(ne):
    spl = f.readline().split('\t')
    edge_weight.append((int(spl[0]), int(spl[1]), int(spl[2])))
f.close()

g = nx.Graph()
g.add_weighted_edges_from(edge_weight)
edge_label = nx.get_edge_attributes(g, 'weight')

nx.draw_networkx(g, pos = vertex_pos, ax = plt.gca(), node_size = 40, font_size = 5)

nx.draw_networkx_edge_labels(g,pos = vertex_pos, edge_labels = edge_label, font_size = 5)

plt.ylim(1.289,1.301)
plt.xlim(103.84,103.851)
plt.axis('off')
plt.savefig('MRT.png', dpi = 720)
plt.show()

starting_node = 16

#Dijktra's Algorithm for Shortest Distance from starting node to every vertex

def Dijkstra(graph, start):
    print("Distance\t\tPath")
    predecessor=defaultdict()
    A = [None] * len(graph)
    queue = [(0, start,None)]
    while queue:
        path_len, v, route = heappop(queue)
        if A[v] is None: 
            predecessor[v]=route
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w,v))
                    
    for end in range(nv):
        j=end
        pred=str(end)
        if end!=start:
            while(predecessor[end]!=start):
                pred=str(predecessor[end])+"\t"+pred
                end=predecessor[end]
            pred=str(start)+"\t"+pred
        print(A[j],"\t\t",pred)



d_adj_basic=defaultdict(dict)
for i in range(ne):
    u, v, w = edge_weight[i]
    d_adj_basic[u][v]=w
    d_adj_basic[v][u]=w

predecessor=Dijkstra(d_adj_basic,starting_node)