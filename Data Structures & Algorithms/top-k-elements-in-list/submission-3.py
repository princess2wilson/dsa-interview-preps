class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        hashmap = {}

        for x in nums:
            hashmap[x] = 1+hashmap.get(x,0)
        for num, count in hashmap.items():
            freq[count].append(num)
        

        res = []
        
        for x in range(len(freq)-1,0,-1):
            for num in freq[x]:
                res.append(num)
                if len(res) == k:
                    return res

        

        
