class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)
        res = []

        for s in strs:
            hmap[tuple(sorted(s))].append(s)

        for val in hmap.values():
            res.append(val)
        return res

        


        