from collections import defaultdict,deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        provinces =0
        n = len(isConnected)

        def dfs(i):
            self.visited.add(i)
            for neighbour in range(n):
                if neighbour not in self.visited and isConnected[i][neighbour] == 1:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in self.visited:
                provinces+=1
                dfs(i)
        return provinces

        
    