import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0

        while q or maxHeap:
            time+=1
            if not maxHeap:
                time = q[0][1]
            else: #theres some stuff in maxheap,lets decrement time and check if any ready?
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: #lets add this first one to the q, with its processing time
                    q.append((cnt,time+n))
            if q and q[0][1] == time: #any ready?
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
