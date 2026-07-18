from collections import defaultdict
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        max_len = 0
        count = 0
        while r<len(nums):

            if nums[r] == 0:
                count+=1
                while count>k:
                    if nums[l] == 0:
                        count-=1
                    l+=1
            
            max_len = max(max_len,r-l+1)
            r+=1
        return max_len
            
            
            
                