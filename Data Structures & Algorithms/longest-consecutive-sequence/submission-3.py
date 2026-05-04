class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_count = 0

        for x in nums:
            nums_set.add(x)
        
        for x in range(len(nums)):
            count = 0
            i=0
            if nums[x] -1 not in nums_set:
                while nums[x]+i in nums_set:
                    count+=1
                    max_count = max(max_count,count)
                    i+=1
        return max_count
                
