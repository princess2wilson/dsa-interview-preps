from collections import defaultdict,deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        if n == 1:
            return [0]


        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a]+=1
            indegree[b]+=1
        for x in indegree:
            if indegree[x] == 1:
                queue.append(x)
        
        
        while len(indegree)>2 and queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                del indegree[node]
                for nei in graph[node]:
                    if nei not in indegree:
                        continue
                    indegree[nei]-=1
                    if indegree[nei]==1:
                        queue.append(nei)
        return list(indegree.keys())













