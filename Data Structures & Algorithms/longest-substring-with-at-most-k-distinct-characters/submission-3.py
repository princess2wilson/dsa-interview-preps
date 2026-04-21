class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_counter = 0
        strings = {}

        l = 0

        for r in range(len(s)):
            strings[s[r]] = 1+strings.get(s[r],0)

            while len(strings) > k:
                strings[s[l]]-=1

                if strings[s[l]] == 0:
                    strings.pop(s[l])
                l+=1
            max_counter = max(max_counter,r-l+1)
        return max_counter
        
       
