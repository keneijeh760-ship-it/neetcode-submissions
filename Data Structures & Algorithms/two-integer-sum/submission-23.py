class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = defaultdict(list)

        for i, num in enumerate(nums):
            dic[num].append(i)

        for key, value in dic.items():
            if target - key in dic and key != target - key:
                return [dic[key][0], dic[target - key][0]]

            elif len(dic[key]) > 1:
                return [dic[key][0], dic[key][1]]
        return

        