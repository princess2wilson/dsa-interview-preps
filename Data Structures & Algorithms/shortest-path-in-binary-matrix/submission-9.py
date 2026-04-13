from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited =set()
        start = (0,0)
        count = 1
        target = (len(grid)-1,len(grid[0])-1)
        if grid[0][0]!=0 or grid[len(grid)-1][len(grid[0])-1]!=0:
            return -1

        queue.append((start,count))

        while queue:
            (x,y),count = queue.popleft()
            if (x,y) == target:
                return count
            if grid[x][y]==0:
                visited.add((x,y))
                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x-1,y+1),(x+1,y+1),(x-1,y-1),(x+1,y-1)]:
                    if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and (nx,ny) not in visited and grid[nx][ny]==0:
                        queue.append(((nx,ny),count+1))

        return -1
                
        


