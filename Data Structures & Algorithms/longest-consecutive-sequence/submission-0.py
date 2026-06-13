class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        res = 0
        for num in nums:
            if num - 1 in check:
                continue
            cnt = 1
            cur = num
            while cur + 1 in check:
                cnt += 1
                cur += 1
            res = max(res, cnt)

        return res