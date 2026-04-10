class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights)-1
        l = 0
        max_water = 0
        while l < r:
            total = (r - l) * min(heights[l], heights[r])
            max_water = max(max_water, total)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
