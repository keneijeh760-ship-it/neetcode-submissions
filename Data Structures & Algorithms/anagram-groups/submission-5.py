class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)
        res = []
        

        for s in strs:
            dic[tuple(sorted(s))].append(s)

        for val in dic.values():
            res.append(val)
        return res

        
        