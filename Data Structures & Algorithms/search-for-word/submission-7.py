class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j, nei,visited): #(0,3,A)
            if nei >= len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or (i,j) in visited or board[i][j]!=word[nei]:
                return
            visited.add((i,j))

            for x,y in directions:
                if dfs(x+i,y+j,nei+1,visited):
                    return True
            visited.remove((i,j))
            return False
            
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if (dfs(row,col,0,set())):
                        return True
        return False









