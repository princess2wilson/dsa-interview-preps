from collections import deque,defaultdict
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        """
        1. bfs to traverse the graph
        2.queueing mechanism, add each neighbour to queue
        3. no visited set but isvalid condition 
        """

        queue = deque()
        graph = defaultdict(list)
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set()
        original = image[sr][sc]
        queue.append((sr,sc))

        while queue:
            row,col = queue.popleft()
            image[row][col] = color
            for x,y in directions:
                dx,dy = x+row,y+col
                if dx>=0 and dx<len(image) and dy>=0 and dy<len(image[0]) and image[dx][dy] == original and (dx,dy) not in visited:
                    visited.add((dx,dy))
                    queue.append((dx,dy))
        
        return image




            

