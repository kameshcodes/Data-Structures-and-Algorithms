#User function Template for python3

class Solution:

        
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, V, adj, visited, dfs_list, node):
        visited[node]=1
        dfs_list.append(node)
        
        for nbr_node in adj[node]:
            if visited[nbr_node]==0:
                self.dfs(V, adj, visited, dfs_list, nbr_node)
        
    def dfsOfGraph(self, V, adj):
        visited = [0 for i in range(V)]
        start_node = 0
        dfs_list = []
        self.dfs(V, adj, visited, dfs_list, start_node)
        return dfs_list
        



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends