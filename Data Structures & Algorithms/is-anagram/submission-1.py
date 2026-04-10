class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h = defaultdict(int)
        for x in s:
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