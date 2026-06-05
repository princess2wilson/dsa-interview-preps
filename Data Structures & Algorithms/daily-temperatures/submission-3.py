class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nge = [0]*len(temperatures)
        stack = []
        
        for i in range(len(temperatures)-1,-1,-1): #i=5
            while stack:
                if temperatures[stack[-1]]>temperatures[i]:
                    nge[i] = stack[-1]-i
                    break
                else:
                    stack.pop()
            else:
                nge[i] = 0
            stack.append(i) 
        return nge
                