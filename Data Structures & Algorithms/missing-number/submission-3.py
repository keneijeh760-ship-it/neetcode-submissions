class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        check = len(nums)
        for i in range(len(nums)):
            if  check in nums:
                check -= 1

        return check

        