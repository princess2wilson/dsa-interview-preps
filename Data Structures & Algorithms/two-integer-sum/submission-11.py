class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, num in enumerate(nums):
            hash_table[num] = index
        
        for index, x in enumerate(nums):
            diff = target - x
            if diff in hash_table and hash_table[diff]!=index:
                return [index,hash_table[diff]]

        return []