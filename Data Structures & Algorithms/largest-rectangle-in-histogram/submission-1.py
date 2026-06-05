class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        nse = [0]*len(heights)
        pse = [0]*len(heights)
        max_rect = 0

        for x in range(len(heights)-1,-1,-1):
            while stack:
                if heights[stack[-1]] < heights[x]:
                    nse[x] = stack[-1]
                    break
                else:
                    stack.pop() 
            else:
                nse[x] = len(heights)  
            stack.append(x)

        stack = []
        for x in range(len(heights)):
            while stack:
                if heights[stack[-1]] < heights[x]:
                    pse[x] = stack[-1]
                    break
                else:
                    stack.pop()
            else:
                pse[x] = -1
            stack.append(x)
        
        for x in range(len(heights)):
            rect = heights[x] *(nse[x] - pse[x] - 1)
            max_rect = max(max_rect,rect)
        return max_rect
        

