from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        hashmap = defaultdict(int)
        max_count = 0

        left = 0

        for right in range(len(s)):
            hashmap[s[right]]+=1

            while len(hashmap)>k:
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            max_count = max(max_count,right-left+1)
        return max_count
            