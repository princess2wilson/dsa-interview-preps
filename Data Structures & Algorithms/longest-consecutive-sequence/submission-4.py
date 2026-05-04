class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        
        for x in nums:
            count = 0
            i=0
            if x -1 not in nums_set:
                while x+i in nums_set:
                    count+=1
                    max_count = max(max_count,count)
                    i+=1
        return max_count
                
