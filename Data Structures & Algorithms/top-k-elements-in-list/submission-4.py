class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []


        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        
        for key, value in hashmap.items():
            freq[value].append(key)
        

        for i in range(len(freq) - 1, 0, -1):

            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
                
                    





            
        