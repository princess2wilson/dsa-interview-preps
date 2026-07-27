class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        
        def dfs(i):
            if i>=len(s):
                res.append(temp.copy())
                return
            for j in range(i,len(s)):
                if ispali(i,j):
                    temp.append(s[i:j+1])
                    dfs(j+1)
                    temp.pop()


        def ispali(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        dfs(0)
        return res
