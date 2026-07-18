class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stack = []

        for x in s:
            if x not in hashmap:
                stack.append(x)
            else:
                if not stack or (stack and hashmap[x]!=stack.pop()):
                    return False
        
        if stack:
            return False
        return True

            
            