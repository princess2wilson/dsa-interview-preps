class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mappings = {"}":"{","]":"[",")":"("}

        for x in list(s):
            if x in mappings:
                if stack and stack[-1] == mappings[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        if not stack:
            return True
        else:
            return False


        

        