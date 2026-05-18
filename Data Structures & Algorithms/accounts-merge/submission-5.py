from collections import defaultdict
class DSU:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self,x):
        if x!=self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)

        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.rank[px]+=self.rank[py]

        else:
            self.par[px] = py
            self.rank[py]+=self.rank[px]
        return True
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        output = []

        hashmap = {}
        for index,account in enumerate(accounts):
            for email in account[1:]:
                if email in hashmap:
                    dsu.union(hashmap[email],index)
                else:
                    hashmap[email]=index
        
        hashmap2 = defaultdict(list)
        for email,index in hashmap.items():
            parent = dsu.find(index)
            hashmap2[parent].append(email)    

        for parent,emails in hashmap2.items():
            name = accounts[parent][0]
            output.append([name]+sorted(emails))
        return output



        
        

    
        
        









