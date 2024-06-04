#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        
        Indegree = {i: 0 for i in range(V)}
        for node in range(V):
            for nbr in adj[node]:
                Indegree[nbr]+=1
    
        q = []
        
        for node in range(V):
            if Indegree[node]==0:
                q.append(node)
        
        cnt = 0
        while len(q)>0:
            popped_node = q.pop(0)
            cnt+=1
            for node in adj[popped_node]:
                Indegree[node]-=1
                if Indegree[node]==0:
                    q.append(node)
        
        return cnt!=V

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends