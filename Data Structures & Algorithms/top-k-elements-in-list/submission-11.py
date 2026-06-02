import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            hashmap[num]+=1
        
        for num,count in hashmap.items():
            freq[count].append(num)
        

        res = []

        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        

