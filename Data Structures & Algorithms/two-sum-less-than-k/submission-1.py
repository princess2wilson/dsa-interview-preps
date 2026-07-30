class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        sorted_nums = sorted(nums)
        max_sum = -1

        l = 0 
        r = len(sorted_nums)-1

        while l<r:
            if sorted_nums[l] + sorted_nums[r] < k:
                max_sum = max(max_sum,sorted_nums[l] + sorted_nums[r])
                l+=1
            else:
                r-=1
        return max_sum
       

            