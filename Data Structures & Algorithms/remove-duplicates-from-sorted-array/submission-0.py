class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,1

        while i < len(nums)-1:
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i = i+1
                j= j+1
        k = len(nums)
        return k