from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        mins=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                    visited.add((row,col))
    
        
        while queue:
            mins+=1
            for level in range(len(queue)):
                x,y = queue.popleft()
                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if nx <0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]) or grid[nx][ny]!=1 or (nx,ny) in visited:
                        continue
                    visited.add((nx,ny))
                    grid[nx][ny] = 2
                    queue.append((nx,ny))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    return -1
        
        return max(mins-1,0)
            
        


        