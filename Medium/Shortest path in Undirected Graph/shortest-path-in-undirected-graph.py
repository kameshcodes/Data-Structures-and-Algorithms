#User function Template for python3
from queue import Queue

class Solution:

        
        
    def shortestPath(self, edges, n, m, src):
        adj = [[] for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False for i in range(n)]
        dist = [-1 for i in range(n)]
        
        q = []
        q.append(src)
        visited[src] = True
        dist[src] = 0
        
        while len(q)>0:
            node = q.pop(0)
            
            for nbr_node in adj[node]:
                if visited[nbr_node]==False:
                    visited[nbr_node] = True
                    dist[nbr_node] = dist[node]+1
                    q.append(nbr_node)
            
        return dist
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends