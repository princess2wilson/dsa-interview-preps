class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        count = 0
        max_count = 0

        while r<len(nums):
            if nums[r] != 1:
                count+=1

                while count > k:
                    if nums[l] == 0:
                        count -=1
                    l+=1
            max_count = max(r-l+1,max_count)
            r+=1
        return max_count
                    







        """
        left and right pointer, right pointer 
        doing the main traversals
        we keep a note of the amount of 0's if we
        """