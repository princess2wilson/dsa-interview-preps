class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_split = [char.lower() for char in s if char.isalnum()]
        l,r = 0, len(s_split)-1
        print(s_split)

        while l<=r:
            if s_split[l] != s_split[r]:
                return False
            l+=1
            r-=1
        return True
