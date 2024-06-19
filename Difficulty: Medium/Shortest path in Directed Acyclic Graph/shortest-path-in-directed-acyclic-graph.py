#User function Template for python3

from typing import List

class Solution:
    def dfs(self, n, adj, visited, node, stack):
        visited[node] = 1
        for nbr in adj[node]:
            if visited[nbr[0]]==0:
                self.dfs(n, adj, visited, nbr[0], stack)
        stack.append(node)
        
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1:]
            adj[u].append(v)
            
        stack = []
        visited = [0 for _ in range(n)]
        
        for node in range(n):
            if visited[node]==0:
                self.dfs(n, adj, visited, node, stack)
                
        distances = [float('inf')] * (n)
        start_node = 0 
        distances[start_node] = 0
        
        while stack:
            node = stack.pop()
            if distances[node] != float('inf'):
                for nbr, weight in adj[node]:
                    if distances[node] + weight < distances[nbr]:
                        distances[nbr] = distances[node] + weight
        
        distances = [-1 if dist == float('inf') else dist for dist in distances]
        
        return distances
        
        

#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends