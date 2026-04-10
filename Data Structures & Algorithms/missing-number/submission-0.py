class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected =sum(range(len(nums)+1))
        actual = sum(nums)

        return expected - actual