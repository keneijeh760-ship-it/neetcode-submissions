class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = sorted(s)
        newT = sorted(t)
        while newS == newT:
            return True
        return False

        
       