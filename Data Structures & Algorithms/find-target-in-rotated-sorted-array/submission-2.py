class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1

        while left<right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid 
       


        pivot = left
        if pivot > 0 and target >= nums[0] and target<=nums[pivot-1]:
            l,r = 0,pivot-1
        else:
            l,r = pivot,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1

