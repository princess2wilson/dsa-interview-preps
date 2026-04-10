class Solution:
    import heapq
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        queue = []
        rows = len(heights) - 1
        cols = len(heights[0]) - 1
        result = 0
        directions =[[1,0],[-1,0],[0,1],[0,-1]]

        start = heights[0][0]


        heapq.heappush(queue,(0,0,0))

        while queue:
            curr_effort,i,j = heapq.heappop(queue)

            if (i,j) in visited:
                continue
            visited.add((i,j))

            if i == rows and j == cols:
                return curr_effort
            
            for di,dj in directions:
                new_i,new_j = i+di, j+dj
                
                if new_i < 0 or new_i > rows or new_j<0 or new_j>cols or (new_i,new_j) in visited:
                    continue
                
                result = max(curr_effort,abs(heights[new_i][new_j] - heights[i][j]))
                heapq.heappush(queue,(result,new_i,new_j))
                
        return 0
                
            
            

            
            



            
        

