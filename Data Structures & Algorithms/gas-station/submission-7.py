class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        start_index = 0
        if total_gas < total_cost:
            return -1
        running = 0
        for i,(g,c) in enumerate(zip(gas,cost)):
            running+=g -c
            if running >= 0:
                continue
            else:
                running = 0
                start_index = i+1
        return start_index
            
        
        

