from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order =[]
        indegree = [0]*numCourses    
        graph = defaultdict(list)   
        for a,b in prerequisites:
            graph[b].append(a)
          
            indegree[a]+=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] ==0:
                queue.append(i)


        def bfs():
            while queue:
                x = queue.popleft()
                order.append(x)
                for neighbour in graph[x]:
                    indegree[neighbour]-=1
                    if indegree[neighbour]==0:
                        queue.append(neighbour)
        bfs()
        if len(order)!=numCourses:
            return []
        return order

                        

                
            


