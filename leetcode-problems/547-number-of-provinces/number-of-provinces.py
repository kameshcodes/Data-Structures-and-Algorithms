from queue import Queue
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def adj_list(V, adj_matrix):
            adj_list_ = [[] for j in range(V)]
            for i in range(V):
                for j in range(V):
                    if adj_matrix[i][j] == 1 and i!=j:
                        adj_list_[j].append(i)
            return adj_list_

        def traverse_bfs(V, visited, adj, start_node):
            q = Queue(maxsize = V)
            q.put(start_node)
            visited[start_node] = 1 
            while q.empty() == False:
                front_node = q.get()
                
                for node in adj[front_node]:
                    if visited[node] == 0:
                        visited[node] = 1
                        q.put(node)
            return visited

        def get_provinces_num(adj_matrix):
            V = len(adj_matrix)
            adj = adj_list(V, adj_matrix)
            visited = [0 for i in range(V)]
            count = 0
            for node in range(V):
                if visited[node]==0:
                    visited = traverse_bfs(V, visited, adj, node)
                    count = count + 1
            return count
        
        count = get_provinces_num(isConnected)
        return count