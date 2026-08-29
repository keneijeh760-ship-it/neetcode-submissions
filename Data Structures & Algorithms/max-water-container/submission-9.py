class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        maxArea = 0
        r =len(heights) - 1

        while l < r:
            Area = (r - l) * min(heights[l], heights[r]) 
            maxArea = max(maxArea, Area)
                
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea






        