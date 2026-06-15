class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for s in strs:
            sort = "".join(sorted(s))
            if sort not in check:
                check[sort] = [s]
            else:
                check[sort].append(s)
        
        res = []

        for key, items in check.items():
            res.append(items)
        
        return res