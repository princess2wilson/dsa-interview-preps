class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        
        for i in range(len(s)):
            p1 = p2 = i
            
            while p1>=0 and p2<len(s) and s[p1] == s[p2]:
                pal = s[p1:p2+1]
                if len(pal)>len(max_pal):
                    max_pal = pal
                p1-=1
                p2+=1
        
        for i in range(len(s)-1):
            p1 = i
            p2 = i+1
            while p1>=0 and p2<len(s) and s[p1] == s[p2]:
                pal = s[p1:p2+1]
                if len(pal)>len(max_pal):
                    max_pal = pal
                p1-=1
                p2+=1
        return max_pal
                    




        