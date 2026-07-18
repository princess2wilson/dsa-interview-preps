from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        curr_sum = 0
        total = 0

        for i,num in enumerate(nums):
            curr_sum+=num

            if curr_sum-k in hashmap:
                total+=hashmap[curr_sum-k]
            hashmap[curr_sum]+=1
        return total
