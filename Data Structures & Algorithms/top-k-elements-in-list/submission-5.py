import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        queue = []
        ans = []

        for x in nums:
            frequency[x] = 1+frequency.get(x,0)
        for num,freq in frequency.items():
            heapq.heappush(queue,((freq),num))
            
            while len(queue)>k:
                heapq.heappop(queue)
        for _ in range(k):   
            freq,x = heapq.heappop(queue)
            ans.append(x)
        return ans        
        

