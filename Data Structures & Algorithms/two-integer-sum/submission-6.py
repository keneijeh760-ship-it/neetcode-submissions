class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store =  []
        count = 0

        for i, num in enumerate(nums):
            if target - num in store:
                
                return [store.index(target - num), i]
            store.append(num)
            count += 1