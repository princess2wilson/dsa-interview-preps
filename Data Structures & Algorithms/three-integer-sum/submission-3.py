class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l,r = 0,len(nums) - 1
        output = []

        for i in range(0,len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r = len(nums)-1
            while l<r:
                sum_ = nums[i] + nums[l] + nums[r]

                if sum_==0:
                    output.append([nums[l],nums[i],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif sum_< 0:
                    l+=1
                elif sum_>0:
                    r-=1
        return output


