class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for char in s:
            if char=="(" or char=="[" or char=="{":
                stack.append(char)
            else:
                if not stack:
                    return False
                popped=stack.pop()
                if popped=="(" and char==")" or popped=="[" and char=="]" or popped=="{" and char=="}":
                    pass
                else:
                    return False
        if not stack:
            return True
