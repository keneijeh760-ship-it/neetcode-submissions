class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = [[] for i in range(len(nums) + 1)]
        topK = []


        for num in nums:
            count[num] =  1 + count.get(num, 0)

        for num, freq in count.items():
            res[freq].append(num)
        
        for i in range(len(res) - 1, 0, -1):
            for val in res[i]:
                topK.append(val)
                if len(topK) == k:
                    return topK



        