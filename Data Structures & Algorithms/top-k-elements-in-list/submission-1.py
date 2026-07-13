class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        count = {}
        res = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, freq in count.items():
            res[freq].append(num)

        r = []

        for i in range(len(res) -1, 0, -1):
            for num in res[i]:
                r.append(num)
                if len(r) == k:
                    return r
            
        