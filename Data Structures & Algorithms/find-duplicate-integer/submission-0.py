from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = set()
        for num in nums:
            if num in hashmap:
                return num
            hashmap.add(num)
            
            