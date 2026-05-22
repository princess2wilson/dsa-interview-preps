class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.s = s
        left= 0 
        right = len(self.s)-1

        while left<right:
            self.swap(left,right)
            left+=1
            right-=1
        
        left = 0
        right = 0
        while right<len(self.s):
            if right == len(self.s)-1 or self.s[right+1] == " ":
                temp_right = right
                while left<right:
                    self.swap(left,right)
                    left+=1
                    right-=1
                right = temp_right+1
                left = temp_right+2
            else:
                right+=1
            
    

    def swap(self,left,right):
        
        temp = self.s[left]
        self.s[left] = self.s[right]
        self.s[right] = temp


    
    
        """
        firstly swap each character using two pointers
        then depending on where the spaces are, we swap again
        the sky is blue
        eulb si yks eht
        """