class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(',']':'[','}':'{'}
        stack = []
        

        for c in s:
            if c not in mapping: #if the bracket is an opening bracket add to stack
                stack.append(c)
            else:
                if not stack or (stack.pop()!=mapping[c]): #if theres no stack that means that
                #there is no more brackets left and therefore we have closed all the brackets, or theres just no opening brackets to begin with anyway
                #or if the last opening bracket dont match the closing bracket youve given me at c
                    return False
        return not stack #if theres anything left, that means we havent closed everything, so theres excess opening brackets
    
            
