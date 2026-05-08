import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_k = right
        
        while left<=right:
            mid = (left+right)//2
            count = 0 
            for x in piles:
                hours = math.ceil((x/mid))
                count+=hours
            if count <=h:
                min_k = min(min_k,mid)
                right = mid - 1
            else:
                left = mid+1
        return min_k
           

            


