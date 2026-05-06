class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        hashmap = {}
        longest = 0

        for right in range(len(s)):
            while s[right] in hashmap:
                hashmap.pop(s[left])
                left+=1
                
            else:
                hashmap[s[right]] = right
            longest = max(longest,hashmap[s[right]] - left+1)
        return longest


