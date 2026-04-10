class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap =set()
        for x in nums:
            if x not in hashmap:
                hashmap.add(x)
            else:
                hashmap.remove(x)
        return list(hashmap)[0]