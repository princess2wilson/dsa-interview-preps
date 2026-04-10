class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for x in range(len(strs[0])):
            for z in strs:
                if x==len(z) or strs[0][x] != z[x]:
                    return res
            res = res + strs[0][x]
            
        return res