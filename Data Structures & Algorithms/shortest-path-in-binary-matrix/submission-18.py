from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = set((0,0))
        queue = deque()
        queue.append((0,0))
        self.count = 0
        if not grid or grid[0][0]!=0 or grid[len(grid)-1][len(grid)-1]!= 0:
            return -1
        def bfs():
            count = 1
            while queue:
                for _ in range(len(queue)):
                    i,j = queue.popleft()
                    if i == len(grid)-1 and j == len(grid)-1:
                        return count 
                    for x,y in directions:
                        if i+x<0 or i+x>=len(grid) or j+y<0 or j+y>=len(grid[0]) or grid[i+x][j+y]!=0 or (i+x,j+y) in visited:
                            continue
                        visited.add((i+x,j+y))
                        queue.append((i+x,j+y))
                count+=1
            return -1

       
        return bfs()