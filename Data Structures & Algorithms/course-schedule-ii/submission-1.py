class Solution:
    from collections import defaultdict,deque
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        order = []

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        for x in range(n):
            if indegree[x] == 0:
                queue.append(x)

        while queue:
            node = queue.popleft()
            order.append(node)
            for x in graph[node]:
                indegree[x]-=1
                if indegree[x] == 0:
                    queue.append(x)
            
        return order if len(order) == n else []



