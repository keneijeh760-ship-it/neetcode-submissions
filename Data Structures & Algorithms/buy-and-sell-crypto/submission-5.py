class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maxP = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            maxP = max(maxP, prices[r] - prices[l])
        return maxP
            
        