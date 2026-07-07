class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        hashset = []
        res = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1


        for num, hashs in hashmap.items() :
            hashset.append([hashs, num])
        hashset.sort()

        while len(res) < k:
            res.append(hashset.pop()[1])
        return res       