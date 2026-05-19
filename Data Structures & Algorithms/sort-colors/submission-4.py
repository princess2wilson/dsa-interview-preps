class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(x,y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp

        white = 0
        blue = len(nums)-1
        x = 0

        while x <= blue:
            if nums[x] == 2:
                swap(blue,x)
                blue-=1
                x-=1
            elif nums[x] == 0:
                swap(white,x)
                white+=1
            x+=1


        



            


        