class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        hashmap = {0:1}
        for num in nums:
            currsum+=num

            diff = currsum-k

            res += hashmap.get(diff,0)
            hashmap[currsum] = 1+hashmap.get(currsum,0)

        return res