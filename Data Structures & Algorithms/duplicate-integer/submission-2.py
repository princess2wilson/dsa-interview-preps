class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        if len(nums)== len(my_set):
            return False
        else:
            return True