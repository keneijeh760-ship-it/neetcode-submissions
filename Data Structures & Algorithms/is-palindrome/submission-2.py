class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []

        for char in s.lower():
            if char.isalnum():
                res.append(char)
            continue
        return res == res[::-1]
        