from collections import deque,defaultdict
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.fresh_fruit = 0
        queue = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        


        def bfs():
            count = 0
            while queue and self.fresh_fruit!=0:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    for i,j in directions:
                        ix,iy = x+i,y+j
                        if ix<0 or ix>=len(grid) or iy<0 or iy>=len(grid[0]) or grid[ix][iy]!=1:
                            continue
                        grid[ix][iy] = 2
                        self.fresh_fruit-=1
                        queue.append((ix,iy))
                count+=1
            return count

                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    self.fresh_fruit +=1
        count = bfs()

        if self.fresh_fruit!=0:
            return -1
        return count
