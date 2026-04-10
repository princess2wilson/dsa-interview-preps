class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i,x in enumerate(nums):
            if x in hash_map and abs(hash_map[x] - i) <=k:
                return True
            else:
                hash_map[x] = i
        return False
        
