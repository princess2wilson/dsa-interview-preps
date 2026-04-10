class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1,p2 = 0,len(nums)-1

        while p1 < p2:
            a = nums[p1] 
            b = nums[p2] 
            if a+b < target:
                p1+=1
            elif a+b > target:
                p2-=1
            else:
                return [p1+1,p2+1]
        return []
        