import random
from bisect import bisect_left

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.cm_sum = []
        total = 0
        for num in self.w:
            total+=num
            self.cm_sum.append(total)
        self.total = total
        

    def pickIndex(self) -> int:
       random_number = random.randint(1,self.total)
       ans = bisect_left(self.cm_sum, random_number)
       return ans

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
#[0,1,3,6,]
#[1,2,3,4,5] 1 is the weight of 0th index
#pick random index in range 0,4
#prob of picking index 2 is 3/15