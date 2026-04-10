class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        rows = len(image)
        cols = len(image[0])
        starting_pixel = image[sr][sc]
        visited = set()

        def dfs(sr,sc):
            if sr < 0 or sr>= rows or sc<0 or sc>= cols or image[sr][sc]!= starting_pixel :
                return
            
            visited.add((sr,sc))
            image[sr][sc] =color
            dfs(sr,sc+1)
            dfs(sr,sc-1)
            dfs(sr+1,sc)
            dfs(sr-1,sc)

        dfs(sr,sc)
        return image
            
            