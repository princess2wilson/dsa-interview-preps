class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]

        #[-4,-1,-1,0,1,2]
        for i, x in enumerate(nums):
            if i and x==nums[i-1]:
                continue
            p1,p2 = i+1,len(nums)-1
            while p1<p2:
                ans = nums[p1] + nums[p2] + x
                if ans < 0:
                    p1+=1
                elif ans > 0:
                    p2-=1
                else:
                    res.append([nums[p1],nums[p2],x])
                    p1+=1
                    while p1<p2 and nums[p1] == nums[p1-1]:
                        p1+=1
        return res
