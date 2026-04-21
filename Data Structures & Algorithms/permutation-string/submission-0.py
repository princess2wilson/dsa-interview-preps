class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        freq = {}

        if len(s1) > len(s2):
            return False
        
        for x in range(len(s1)):
            freq[s1[x]] = 1+freq.get(s1[x],0)
            window[s2[x]] = 1+window.get(s2[x],0)
        
        if window == freq:
            return True
        
        l = 0

        for r in range(len(s1),len(s2)):
            window[s2[r]] = 1+ window.get(s2[r],0)
            window[s2[l]]-=1

            if window[s2[l]] == 0:
                window.pop(s2[l])
            l+=1

            if window == freq:
                return True
        return False







