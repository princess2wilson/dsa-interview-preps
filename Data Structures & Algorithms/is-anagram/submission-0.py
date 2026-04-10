class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = defaultdict(int)
        for x in list(s):
            h[x] +=1
        

        for x in list(t):
            if x not in h:
                return False
            else:
                h[x]-=1
        
        for x in h:
            if h[x]!=0:
                return False
        return True