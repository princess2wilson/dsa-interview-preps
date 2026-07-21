class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        from functools import lru_cache
        @lru_cache(None)
        def recurse(i, j):
            if j < 0:
                return i < 0

            if p[j] == "*":
                if recurse(i, j - 2):
                    return True
                if i >= 0 and (p[j-1] == s[i] or p[j-1] == "."):
                    return recurse(i - 1, j)
                return False

            if i >= 0 and (p[j] == s[i] or p[j] == "."):
                return recurse(i - 1, j - 1)
            return False

        return recurse(n - 1, m - 1)