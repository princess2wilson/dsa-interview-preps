class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max_height = 0

        while l<r:
            min_height = min(heights[r],heights[l])
            max_height = max(max_height,min_height*(r-l))

            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        return max_height

