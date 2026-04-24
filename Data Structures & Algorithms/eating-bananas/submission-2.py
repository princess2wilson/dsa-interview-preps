from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        res = max(piles)
        

        while low<=high:
            hours = 0
            mid = (low+high)//2
            for x in (piles):
                hours+=ceil(x/mid)
            if hours <=h:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res
            

