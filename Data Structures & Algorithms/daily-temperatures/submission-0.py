class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack =[]
        for i,temp in enumerate(temperatures):
            while stack:
                if temp > stack[-1][0]:
                    res[stack[-1][1]] = (i-stack[-1][1])
                    stack.pop()
                else:
                    break
                

            stack.append([temp,i])
        return res



