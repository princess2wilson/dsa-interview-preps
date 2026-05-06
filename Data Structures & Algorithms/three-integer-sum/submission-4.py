class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = 0
        res = []
        nums.sort()

        def twosum(left,right,x):
            while left<right and right<len(nums):
                ans = nums[left]+nums[right]
                if 0 - ans == nums[x]:
                    res.append([nums[left],nums[right],nums[x]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:  # add this
                        left += 1
                    while left < right and nums[right] == nums[right+1]:  # add this
                        right -= 1
                elif 0 - ans > nums[x]:
                    left+=1
                else:
                    right-=1

        for x in range(len(nums)-1):
            left = x+1
            right = len(nums)-1
            if x > 0 and nums[x] == nums[x-1]:  # add this
                continue
            two_sum = twosum(left,right,x)
        return res



            