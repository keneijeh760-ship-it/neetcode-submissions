class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sortedT = sorted(t)
        sortedS = sorted(s)

        if sortedS == sortedT:
            return True
        return False