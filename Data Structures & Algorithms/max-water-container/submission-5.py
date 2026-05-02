class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum = 0

        while left < right:
            container = (right - left) * min(heights[left], heights[right])
            maximum = max(container, maximum)
            if heights[right] > heights[left]:
                left+=1
            else:
                right-=1
        return maximum
