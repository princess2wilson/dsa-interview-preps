class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while low<high:
            mid = (low+high)//2

            if nums[mid]>nums[high]:
                low =mid+1
            else:
                high = mid
        pivot = low
                

        def binarysearch(low,high):
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        result = binarysearch(0, pivot - 1)
        if result != -1:
            return result

        return binarysearch(pivot, len(nums) - 1)






