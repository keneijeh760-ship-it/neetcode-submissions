class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []
       


        for i, num in enumerate(nums):
            if target - num in res:
                return [ res.index(target-num), i]
            res.append(num)
        return
                
        
            

        