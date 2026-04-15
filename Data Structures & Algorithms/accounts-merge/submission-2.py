class DSU:
    def __init__(self,accounts):
        n = len(accounts)
        self.par = [i for i in range(n)]
        self.rank = [1] *n
    
    def find(self,node):
        while node!=self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node
    
    def union(self,node1,node2):
        p1,p2 = self.find(node1),self.find(node2)
        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.rank[p1]+=self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.par[p1] = p2
        return True    
    


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(accounts)
        hashmap = {}
        for index,account in enumerate(accounts):
            for email in account[1:]:
                if email in hashmap:
                    dsu.union(index,hashmap[email])
                else:
                    hashmap[email] = index
        
        emailGroup = defaultdict(list)
        for email,i in hashmap.items():
            leader = dsu.find(i)
            emailGroup[leader].append(email)


        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res

        
      



            
            
        











