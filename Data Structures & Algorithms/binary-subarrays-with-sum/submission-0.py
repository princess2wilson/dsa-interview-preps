class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #count num of subarrarys where currsum <=x
        def helper(x):
            if x < 0 : return 0

            res =0 
            l=0
            curr_sum = 0

            for r in range(len(nums)):
                curr_sum+=nums[r]

                while curr_sum > x:
                    curr_sum-=nums[l]
                    l+=1
                res+=(r-l+1)
            return res


        return helper(goal) - helper(goal - 1)
        
        #notes:
        #the lenght of the array = number of subarrays
        # number of arrays less than or equal to gaol - number
        # of arrays less than or equal to goal - 1 gives you the number of goals
        # exactly equal to goal.


            
