#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        
        start_node = 0
        q = Queue(maxsize=V)
        visited = [0 for i in range(V)]
        bfs_list = []
        
        visited[start_node] = 1
        q.put(start_node)
        
        while q.empty() == False:
            popped_node = q.get()
            bfs_list.append(popped_node)
            
            for node in adj[popped_node]:
                if visited[node] == 0:
                    visited[node] = 1
                    q.put(node)
                    
        return bfs_list
            
        

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends