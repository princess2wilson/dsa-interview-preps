from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        visited = set() #TODO

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row,col))

        while queue:
            i,j = queue.popleft()
            for x,y in directions:
                dx,dy = i+x,j+y 
                if dx<0 or dx>=len(grid) or dy<0 or dy>=len(grid[0]) or grid[dx][dy]!= 2147483647:
                    continue
                grid[dx][dy] = grid[i][j]+1
                queue.append((dx,dy))





                   
        

                    

        