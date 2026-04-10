class dsu:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        r1,r2 = self.find(x),self.find(y)
        if r1 == r2:
            return False
        if self.rank[r1] < self.rank[r2]:
            self.parent[r1] = r2
            self.rank[r2]+=self.rank[r1]
        else:
            self.parent[r2] = r1
            self.rank[r1]+=self.rank[r2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = dsu(len(accounts))
        emailToAcc = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(emailToAcc[email],i)
                else:
                    emailToAcc[email]= i

        merged = defaultdict(list)
        res = []
        for email,index in emailToAcc.items():
            parent = uf.find(index) 
            merged[parent].append(email)
        
        for index,emails in merged.items():
            account_name = accounts[index][0]
            emails.sort()
            emails.insert(0,account_name)
            res.append(emails)

        return(res)