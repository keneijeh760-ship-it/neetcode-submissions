class Solution:
    def isValid(self, s: str) -> bool:

        brackets =  {')': '(', '}': '{', ']':'['}
        stk = []


        for char in s:
            if char in brackets:
                if not stk:
                    return False
                top = stk.pop()
                if brackets[char] != top:
                    return False
                     

            else:
                stk.append(char)
        
        if stk:
            return False
        else:
            return True

        