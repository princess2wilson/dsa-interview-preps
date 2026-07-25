class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        total = 0
        start = 0
        
        for index,(g,c) in enumerate(zip(gas,cost)):
            total +=(g-c)
            if total<0:
                total = 0
                start = index+1
            
        return start

        