import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []

        for x in nums:
            heapq.heappush(queue,x)
            while len(queue) > k:
                heapq.heappop(queue)
        return queue[0]
