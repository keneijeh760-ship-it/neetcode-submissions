class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        count = 0
        maxLen = 0
        hashmap = {}
        
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            count = max(count, hashmap[s[r]])

            while (r - l + 1)  - count > k:
                hashmap[s[l]] -= 1
                l += 1
                

            maxLen = max(maxLen, r-l + 1)
        return maxLen
        

            
            
            


        