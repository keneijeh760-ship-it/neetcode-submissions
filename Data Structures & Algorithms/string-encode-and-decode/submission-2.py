class Solution:

    def encode(self, strs: List[str]) -> str:

        nstr = ""

        for s in strs:
            nstr += str(len(s)) + '#' + s
        return nstr
    def decode(self, s: str) -> List[str]:

        res = []
        r = 0

        while r < len(s):
            l = r

            while s[l] != '#':
                l += 1
            length = int(s[r:l])

            r = l + 1
            l = r + length
            res.append(s[r:l])
            r = l
        return res
