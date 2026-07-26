class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = set()

        right = left = max_lenght= 0

        for right in range(len(s)):
            while s[right] in char_map:
                char_map.remove(s[left])
                left+=1
            
            char_map.add(s[right])
            max_lenght = max(max_lenght,right-left+1)
        return max_lenght