class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [],[]
        res = []
        for x in nums:
            if x > 0:
                pos.append(x)
            else:
                neg.append(x)
        
        i = 0

        while i < len(nums)//2:
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
            i+=1
        return nums