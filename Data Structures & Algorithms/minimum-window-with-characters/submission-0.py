class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l=0
        window = {}
        freq = {}
        counter = 0
        min_count = float("inf")
        res = ""
        for x in t:
            freq[x] = 1+freq.get(x,0)

        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r],0)
            if s[r] in freq and window[s[r]]==freq[s[r]]:
                counter+=1
            
            while counter == len(freq):
                if min_count > (r-l+1):
                    min_count = r-l+1
                    res = s[l:r+1]
                window[s[l]]-=1
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    counter -= 1 
                l+=1
        return res
            