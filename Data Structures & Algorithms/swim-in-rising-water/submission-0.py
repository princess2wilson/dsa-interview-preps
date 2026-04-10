class Solution:
    from collections import defaultdict
    import heapq
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        N = len(grid)
        target = (N-1,N-1)
        t=0

        #for heapq, it expects a list of tuples like (priority, x, y).
        queue = [(grid[0][0],(0,0))]

        while queue:
            cost, (i,j) = heapq.heappop(queue)
            t = max(cost,t)
            visited.add((i,j))
                
            if (i,j) == target:
                return t
            

            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < N and 0 <= y < N and (x, y) not in visited:
                    heapq.heappush(queue, (grid[x][y], (x, y)))
            