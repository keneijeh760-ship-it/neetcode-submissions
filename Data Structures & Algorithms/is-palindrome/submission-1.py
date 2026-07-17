class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr = ""

        for c in s.lower():
            if c.isalnum():
                nstr += c
            continue
        return nstr == nstr[::-1]

        