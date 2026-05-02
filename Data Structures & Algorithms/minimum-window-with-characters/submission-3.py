class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        win = {}
        t_count = Counter(t)
        left,right =0,0
        min_ = ""


        while right<len(s):
            win[s[right]] = 1+win.get(s[right],0)

            while all(win.get(char, 0) >= count for char, count in t_count.items()):
                if min_ == "" or len(min_)> len(s[left:right+1]):
                    min_ = s[left:right+1]
               
                win[s[left]] -=1
                
                if win[s[left]]==0:
                    win.pop(s[left])
                left+=1
            right+=1
        return min_




    
        