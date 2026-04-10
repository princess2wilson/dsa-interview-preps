class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,v in enumerate(nums):
            hashmap[v] = i
        
        for i,v in enumerate(nums):
            diff = target - v
            if diff in hashmap and i!=hashmap[diff]:
                return [i,hashmap[diff]]
            