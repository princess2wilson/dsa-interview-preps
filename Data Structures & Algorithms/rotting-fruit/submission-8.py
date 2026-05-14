from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions =[(0,1),(0,-1),(1,0),(-1,0)]
        self.fresh_count = 0
        def bfs():
            count = 0
            
            if self.fresh_count == 0:
                return 0

            while queue and self.fresh_count>0:
                for _ in range(len(queue)):
                    i,j = queue.popleft()
                    for x,y in directions:
                        if isValid(i+x,j+y):
                            grid[i+x][j+y] = 0
                            self.fresh_count-=1
                            queue.append((i+x,j+y))
                count+=1
                
            if count == 0 or self.fresh_count!=0:
                return -1
            else:
                return count
                        
        
        def isValid(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
                return False
            return True



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    self.fresh_count+=1
        return bfs()
    


    """
    Psuedocode bfs solution with levelling count:
    1. we need to mark each one we visited as a 0 so we dont visit it again.
    2. we need levelling so a for loop on the queue which is a deque
    3. we need directions array to loop over directions
    4. we need add neighbours but check before adding neighbour.
    """