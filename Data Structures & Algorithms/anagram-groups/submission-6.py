class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        freq = []

        for char in strs:
            hashmap[tuple(sorted(char))].append(char)

        for value in hashmap.values():
            freq.append(value)

        return freq

        
        

        