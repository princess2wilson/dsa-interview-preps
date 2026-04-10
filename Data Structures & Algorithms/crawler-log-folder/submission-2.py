class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0 #we are already in main

        for x in logs:
            if x == "../": 
                res = max(0, res-1) #the max is 0, but -1 if possible
            elif x == "./": #dont do anything
                continue
            else:
                res = res+1
        return res

