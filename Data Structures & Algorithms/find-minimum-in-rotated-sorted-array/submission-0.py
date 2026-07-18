class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        nums.sort()

        while l <= r:
            mid =  l + ((r-l)//2)

            if nums[mid] == min(nums):
                return nums[mid]
            elif nums[mid] < min(nums):
                l = mid + 1
            else:
                r = mid - 1
        return nums[mid]

        