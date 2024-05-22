from typing import List
from queue import Queue

def adj_list(V, edges):
    adj = [[] for i in range(V)]
    for edge in edges:
        nodea = edge[0]
        nodeb = edge[1]
        adj[nodea].append(nodeb)
        adj[nodeb].append(nodea)
    return adj

def bfs_traverse(V, adj, start_node, visited):
    q = Queue(maxsize = V)
    q.put(start_node)
    visited[start_node] = 1
    bfs = []
    while q.empty() == False:
        front_node = q.get()
        bfs.append(front_node)
        
        for node in adj[front_node]:
            if visited[node]==0:
                visited[node]=1
                q.put(node)
    return bfs, visited 

def connected_component(V, edges):
    
    component_count = 0
    adj = adj_list(V, edges)
    visited = [0 for i in range(V)]

    for node in range(V):
        if visited[node] == 0:
            component_count = component_count + 1
            _, visited = bfs_traverse(V, adj, node, visited)
            
    return component_count
            
            
V = 8        
edges =  [(0, 1), (1, 2), (1, 3), (2, 4), (5, 6)]

print(connected_component(V, edges))
