class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        res = cur = 0
        l = 0
        for i in range(len(s)):
            if s[i] in check:
                while l <= i and s[i] in check:
                    check.remove(s[l])
                    l += 1
                    cur -= 1
            check.add(s[i])
            cur += 1
            res = max(res, cur)
        return res
