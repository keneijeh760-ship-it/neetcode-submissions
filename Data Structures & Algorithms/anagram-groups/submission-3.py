class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        res = []

        for s in strs:
            hashmap[tuple(sorted(s))].append(s)

        for values in hashmap.values():
            res.append(values)
        return res


        
        