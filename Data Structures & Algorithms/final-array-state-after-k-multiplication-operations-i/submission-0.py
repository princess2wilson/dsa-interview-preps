class Solution:
    import heapq
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums.copy()
        min_heap = [(num,index)for index,num in enumerate(nums)]
        heapq.heapify(min_heap)
        
        for count in range(k):
            value,index = heapq.heappop(min_heap)
            res[index] *= multiplier
            heapq.heappush(min_heap,(res[index],index))
        return res
