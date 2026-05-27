class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        result = [0] * len(temperatures)
        for x in range(len(temperatures)):
            while stack:
                if temperatures[x]>temperatures[stack[-1]]:
                    result[stack[-1]] = (x-stack[-1])
                    stack.pop()
                else:
                    break
            stack.append(x)
        return result
