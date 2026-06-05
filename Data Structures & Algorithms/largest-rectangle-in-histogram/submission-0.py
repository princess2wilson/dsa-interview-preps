class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pse =[0]*len(heights)
        nse = [0]*len(heights)
        stack = []

        for i in range(len(heights)-1,-1,-1):
            while stack:
                if heights[stack[-1]] < heights[i]:
                    nse[i] = stack[-1]
                    break
                else:
                    stack.pop()
            else:
                nse[i] = len(heights)
            stack.append(i)
        stack = []
        for i in range(len(heights)):
            while stack:
                if heights[stack[-1]] < heights[i]:
                    pse[i] = stack[-1]
                    break
                else:
                    stack.pop()
            else:
                pse[i] = -1
            stack.append(i)
        max_rect = 0
        for x in range(len(heights)):
            rect = heights[x]*(nse[x]-pse[x]-1)
            max_rect = max(max_rect,rect)
        return max_rect



       