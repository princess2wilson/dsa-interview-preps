class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        def convert(n):
            if n == 0:
                return ""
            ans = (n - 1) % 26
            first = (n - 1) // 26
            return convert(first) + chr(ans + ord('A'))

        return convert(columnNumber)