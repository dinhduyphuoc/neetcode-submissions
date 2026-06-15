class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        cur = 0
        for n in s:
            if n - 1 not in s:
                x = n
                cur = 1
                while x + 1 in s:
                    cur += 1
                    x += 1
                res = max(res, cur)
        
        return res
