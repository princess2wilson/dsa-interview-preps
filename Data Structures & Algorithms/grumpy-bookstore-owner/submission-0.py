class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = window = 0
        max_window = 0
        l = 0

        for x in range(len(customers)):

            if grumpy[x]:
                window+=customers[x]
            else:
                satisfied+=customers[x]
            
            if x-l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l+=1
            


            max_window = max(window,max_window)
        
        return satisfied + max_window
