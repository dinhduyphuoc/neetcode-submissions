class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        sample = strs[0]
        
        for i in range(len(sample)):
            for st in strs:
                if i >= len(st):
                    return res
                if sample[i] != st[i]:
                    return res
            res += st[i]
        
        return res