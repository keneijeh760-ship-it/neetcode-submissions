class Solution:
    def isPalindrome(self, s: str) -> bool:

        nstr = ""

        for c in s:
            if c.isalnum():
                nstr += c.lower()
            continue
        return nstr == nstr[::-1]
        