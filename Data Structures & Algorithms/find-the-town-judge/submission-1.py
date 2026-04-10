class Solution:
    from collections import defaultdict
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)


        #must not trust anyone, everyone must trust it
        for a,b in trust:
            indegree[a]+=1 #a trusts +1 person
            outdegree[b]+=1 #b has one trustee


        for x in range(1,n+1):
            if indegree[x] == 0 and outdegree[x] == n-1:
                return x
        return -1