#User function Template for python3
from queue import Queue

class Solution:
    def get_adj(self, n, edges):
        adj = [[] for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)
        return adj
        
        
        
    def shortestPath(self, edges, n, m, src):
        adj = self.get_adj(n, edges)
        visited = [0 for i in range(n)]
        dist = [-1 for i in range(n)]
        q = Queue(maxsize=n)
        
        visited[src] = 1
        dist[src] = 0
        q.put(src)
        
        while q.empty()==False:
            popped_node = q.get()
            
            for node in adj[popped_node]:
                if visited[node]==0:
                    dist[node] = dist[popped_node]+1
                    visited[node]=1
                    q.put(node)
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