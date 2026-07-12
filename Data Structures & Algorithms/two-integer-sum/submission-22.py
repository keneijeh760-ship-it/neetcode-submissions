class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumS = defaultdict(list)

        for i, num in enumerate(nums):
            sumS[num].append(i)

        for keys in sumS.keys():
            if target - keys in sumS.keys():
                
                if keys != target - keys:
                    return [sumS[keys][0], sumS[target-keys][0]]
                elif len(sumS[keys]) > 1:
                    return [sumS[keys][0], sumS[keys][1]]
        return

        