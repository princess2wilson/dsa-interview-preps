class Solution: #IV
    def romanToInt(self, s: str) -> int:
        hashmap ={"I":1,"V":5,"X":10, "L":50,"C":100,"D":500,"M":1000}
        res = 0

        for x in range(len(s)):
            if x+1<len(s) and hashmap[s[x]]<hashmap[s[x+1]]:
                res = res-hashmap[s[x]]
            else:
                res = res+hashmap[s[x]]
        return res

        
