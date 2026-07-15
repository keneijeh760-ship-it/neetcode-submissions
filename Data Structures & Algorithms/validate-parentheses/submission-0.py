class Solution:
    def isValid(self, s: str) -> bool:

        res =[]

        brackets = {']' : '[', '}' : '{', ')': '('}

        for char in s:
            if char in brackets:
                if not res:
                    return False
                top = res.pop()
                if brackets[char] != top:
                    return False

            else:
                res.append(char)

        if res:
            return False
        else:
            return True
        