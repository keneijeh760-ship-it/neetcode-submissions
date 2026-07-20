class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count1 = {}
        count2 = {}

        for char in s:
            count1[char] = 1 + count1.get(char, 0)

        for char in t:
            count2[char] = 1 + count2.get(char, 0)

        if count1.items() == count2.items():
            return True
        return False
        