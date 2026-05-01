from collections import defaultdict,deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        mins = 0
        fresh_count =0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh_count+=1

        while queue and fresh_count >0:
            size = len(queue)
            for _ in range(size):
                i,j = queue.popleft()
                for x,y in directions:
                    if i+x>=0 and i+x<len(grid) and j+y>=0 and j+y<len(grid[0]) and grid[i+x][j+y]==1:
                        grid[x+i][y+j] = 2
                        fresh_count-=1
                        queue.append((i+x,j+y)) 
            mins+=1
        if fresh_count !=0:
            return -1
        return mins

        