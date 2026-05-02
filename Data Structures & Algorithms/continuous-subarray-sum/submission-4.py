class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}
        total = 0

        for x in range(len(nums)):
            total+=nums[x]
            k_total = total%k
            if k_total in prefix and x-prefix[k_total]>=2:
                return True
            else:
                prefix[k_total] = prefix.get(k_total,x)
        return False
            


