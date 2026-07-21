import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        arr = []

        for r in range(len(nums)):
            heapq.heappush(queue,(-nums[r],r))

            if r>=k-1:
                while queue[0][1]<r-k+1:
                    heapq.heappop(queue)
                arr.append(-queue[0][0])
                
        
        return arr

            


