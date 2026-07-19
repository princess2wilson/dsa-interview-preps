class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        curr = prev = res = 0

        curr_op = '+'

        while i<len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    curr = curr*10+int(s[i]) #14
                    i+=1
                i-=1
                if curr_op =='+':
                    res+=curr
                    prev = curr
                elif curr_op == '-': #res =14-3=11,prev = -3
                    res-=curr
                    prev = -curr
                elif curr_op == '*':
                    res-=prev
                    res+=prev*curr
                    prev = curr*prev
                else:
                    res-=prev #res = 11+3 = 14
                    res+=int(prev/curr) #-3//2 = -1 res = 14-1 = 13
                    prev =int(prev/curr) #3//2 = 1
                curr = 0
            elif s[i]!=" ":
                curr_op = s[i]
            i+=1
        return res
