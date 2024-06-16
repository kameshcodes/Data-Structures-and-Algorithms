#User function Template for python3

class Solution:
    
    def get_adj_list(self,n, edges):
        adj = [[] for i in range(n)]
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        return adj
        


    def shortestPath(self, edges, n, m, src):
        #write your code here 
        dist = [-1 for i in range(n)]
        visited = [0 for i in range(n)]
        
        adj = self.get_adj_list(n, edges)
        
        q = []
        q.append(src)
        dist[src]=0
        visited[src] = 1
        
        while len(q) > 0:
            node = q.pop(0)
            
            for nbr_node in adj[node]:
                if visited[nbr_node]==0:
                    visited[nbr_node]=1
                    q.append(nbr_node)
                    dist[nbr_node] = dist[node] + 1
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