import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hashmap = {}
        queue = []
        ans = []

        
        for num in nums:
            hashmap[num] = 1+hashmap.get(num,0)
        
        for num, count in hashmap.items():
            heapq.heappush(queue,(-count,num))
        
        for _ in range(k):
            ans.append(heapq.heappop(queue)[1])
        return ans




        





