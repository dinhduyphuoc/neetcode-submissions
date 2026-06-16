class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        l = 0
        maxFreq = 0
        res = 0
        for r in range(len(s)):  
            check[s[r]] = check.get(s[r], 0) + 1
            maxFreq = max(maxFreq, check[s[r]])
            while (r - l + 1) - maxFreq > k:
                check[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res            
