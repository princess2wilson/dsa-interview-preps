class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        subarrays = 0
        hashmap = {}
        hashmap[0] = 1

        for num in nums:
            total+=num
            k_total = total - k
            if k_total in hashmap:
                subarrays+= hashmap[k_total]
            hashmap[total] = 1+hashmap.get(total,0)
        return subarrays


            
