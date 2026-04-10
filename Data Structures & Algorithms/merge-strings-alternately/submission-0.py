class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2) #abcf, je
        res = ""

        i = j = 0

        while i < n or j < m: 
            
            if i < n:
                res = res+word1[i] #a
            if j<m:
                res = res+word2[j] #aj
            i+=1
            j+=1
        return res
