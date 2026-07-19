class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ng = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1,-1,-1):
            while stack:
                if temperatures[stack[-1]]>temperatures[i]:
                    ng[i]=(stack[-1]-i)
                    break
                else:
                    stack.pop()
            stack.append(i) 
        return ng
