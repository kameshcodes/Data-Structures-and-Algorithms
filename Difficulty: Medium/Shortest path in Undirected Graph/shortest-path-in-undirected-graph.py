#User function Template for python3
from queue import Queue #FiFo

class Solution:
    def shortestPath(self, edges, n, m, src):
        # create adjacency list
        adj = [[] for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)
            
        # \\bfs along with distance addition
        visited = [0 for i  in range(n)]
        dist = [-1 for i in range(n)]
        
        q = Queue(maxsize=n)
        q.put(src)
        dist[src]=0
        visited[src]=1
        while q.empty() == False:
             popped = q.get()
             for nbr in adj[popped]:
                 if visited[nbr]==0:
                     q.put(nbr)
                     visited[nbr]=1
                     dist[nbr] = dist[popped]+1
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