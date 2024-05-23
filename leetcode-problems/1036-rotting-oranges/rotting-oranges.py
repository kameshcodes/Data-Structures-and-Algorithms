from typing import List
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue(maxsize = (len(grid)*len(grid[0])))
        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    visited[i][j]=2
                    q.put([[i, j], time])
        tm = 0
        while q.empty()==False:
            front = q.get()
            row = front[0][0]
            col = front[0][1]
            time = front[1]
            tm = max(time, tm)

            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            for i in range(4):
                new_row = row + delta_r[i]
                new_col = col + delta_c[i]
                if (0<=new_row<len(grid) and 0<=new_col<len(grid[0])) and (grid[new_row][new_col] == 1 and visited[new_row][new_col]!=2):
                    visited[new_row][new_col] = 2
                    q.put([[new_row, new_col], time+1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]!=2 and grid[i][j]==1:
                    return -1
        return tm
                    
        
