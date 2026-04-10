class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        maxCount = 0
        count = 1

        for x in range(len(nums)):
            count = 1
            num = nums[x]
            if num - 1 not in numSet:
                count = 1
            while num + 1 in numSet:
                count +=1
                num = num+1
            maxCount = max(maxCount,count)
        return maxCount

