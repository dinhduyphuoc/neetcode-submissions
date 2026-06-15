class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in check:
                check[key] = [s]
            else:
                check[key].append(s)
        
        res = []

        for key, val in check.items():
            res.append(val)
        
        return res