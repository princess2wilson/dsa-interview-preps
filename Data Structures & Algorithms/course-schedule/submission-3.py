class Solution:
    from collections import deque, defaultdict
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
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
        return len(order) == n

            





        
