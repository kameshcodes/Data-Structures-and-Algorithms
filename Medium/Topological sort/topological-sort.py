from queue import LifoQueue
class Solution:
    
    #Function to return list containing vertices in Topological order.
    
    def dfs(self, V, adj, visited, stack, node):
        visited[node] = 1
        for node_ in adj[node]:
            if visited[node_]==0:
                self.dfs(V, adj, visited, stack, node_)
        stack.put(node)




    def topoSort(self, V, adj):
        stack = LifoQueue(maxsize=V)
        visited = [0 for i in range(V)]
        for i in range(V):
            if visited[i] == 0:
                self.dfs(V, adj, visited, stack, node=i)
        
        
        topo = []
        while stack.qsize()>0:
            topo.append(stack.get())
        
        return topo
        
    

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends