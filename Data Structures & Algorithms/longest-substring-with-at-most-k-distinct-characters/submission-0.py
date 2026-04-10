class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_counter = 0
        l = 0
        counter = collections.Counter()
        max_count = 0 

        for r in range(len(s)):
            counter[s[r]]+=1
            while len(counter) > k :
                counter[s[l]]-=1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l+=1
            max_count = max(r-l+1,max_count)
        return max_count
        
