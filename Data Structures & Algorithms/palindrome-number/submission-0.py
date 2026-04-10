class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = 0
        r = 0

        return ((str(x))==(str(x)[::-1]))