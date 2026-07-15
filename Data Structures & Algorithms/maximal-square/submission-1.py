class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.min_side = 0

        def recurse(i,j):
            if i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]!="1":
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            down = recurse(i+1,j)
            left = recurse(i,j+1)
            diagonal = recurse(i+1,j+1)
            
            dp[i][j] = 1+min(down,left,diagonal)
           
            self.min_side = max(self.min_side,dp[i][j])
            return dp[i][j]

        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                recurse(i,j)

        return self.min_side*self.min_side

            