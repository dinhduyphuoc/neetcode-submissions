class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            check.add(s[r])
        
        return res