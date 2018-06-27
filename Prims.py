import heapq
import networkx as nx
import numpy as np
from collections import defaultdict

vertex_pos = {}
edge_weight = []

f = open('Graph.graph', 'r')
spl = f.readline().split('\t')
nv, ne = int(spl[0]), int(spl[1])

for i in range(ne):
    spl = f.readline().split('\t')
    edge_weight.append((int(spl[0]), int(spl[1]), int(spl[2])))
f.close()

g = nx.Graph()
g.add_weighted_edges_from(edge_weight)
edge_label = nx.get_edge_attributes(g, 'weight')

starting_node = 16
tree_node = [starting_node]
tree_edge = []
heap = []
for e in g.edges(starting_node, data = True):
    if e[1] not in tree_node:
        heapq.heappush(heap, (e[2]['weight'], (e[0], e[1])))

while len(tree_node) != nv:
    eweight, nodepair = heapq.heappop(heap)
    while nodepair[1] in tree_node:
        eweight, nodepair = heapq.heappop(heap)
    tree_node.append(nodepair[1])
    tree_edge.append((nodepair[0], nodepair[1]))
    for e in g.edges(nodepair[1], data = True):
        if e[1] not in tree_node:
            heapq.heappush(heap, (e[2]['weight'], (e[0], e[1])))
    

d_tree=defaultdict(list)
for ed in tree_edge:
    d_tree[ed[0]].append(ed[1])
    d_tree[ed[0]].sort()
    
traverse=[]
def preOrder(root):
    if root not in traverse:
        traverse.append(root)
    sub_tree=[]
    i=0
    if root in d_tree:
        while i!=len(d_tree[root]):
            heapq.heappush(sub_tree,d_tree[root][i])
            i=i+1
        root1=heapq.heappop(sub_tree)
        preOrder(root1)
        heapq.heappop(d_tree[root])
        if len(d_tree[root])!=0:
            preOrder(root)
    return root   

r=preOrder(starting_node)
print(traverse) 