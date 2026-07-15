class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def recurse(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + recurse(i+1,j+1)
                return dp[i][j]
            dp[i][j] = max(recurse(i+1,j),recurse(i,j+1))
            return dp[i][j]
        dp = [[-1]*len(text2) for _ in range(len(text1))]
        return recurse(0,0)
            