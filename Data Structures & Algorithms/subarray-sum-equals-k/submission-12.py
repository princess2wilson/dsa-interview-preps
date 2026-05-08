class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        total = 0
        for num in nums:
            total+=num
            ktotal = total - k

            if ktotal in hashmap:
                count+=hashmap[ktotal]
            hashmap[total] = 1+hashmap.get(total,0)
        return count


