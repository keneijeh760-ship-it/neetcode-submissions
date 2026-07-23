class Solution:
    def isValid(self, s: str) -> bool:

        dic = {')': '(', '}': '{', ']':'['}
        stack = []

        for char in s:

            if char in dic:
                if not stack:
                    return False
                top = stack.pop()
                if top != dic[char]:
                    return False

            else:
                stack.append(char)  
        if stack:
            return False
        return True   