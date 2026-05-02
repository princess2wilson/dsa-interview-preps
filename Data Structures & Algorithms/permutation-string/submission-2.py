class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        win = {}
        s1_hash = {}
        for x in range(len(s1)):
            s1_hash[s1[x]] =  1+ s1_hash.get(s1[x],0)
        
        left,right =0,len(s1)-1

            
        for x in range(left,right+1):
            win[s2[x]] =  1+ win.get(s2[x],0)


        while right < len(s2):
            if win == s1_hash:
                return True
            win[s2[left]]-=1
            if win[s2[left]] == 0:
                win.pop(s2[left])
            left+=1
            right+=1
            if right<len(s2):
                win[s2[right]] =  1+ win.get(s2[right],0)
        return False

