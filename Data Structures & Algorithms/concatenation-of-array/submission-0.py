class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)

        k = 0

        while k < len(res):
            i = k % len(nums)
            res[k] = nums[i]
            k += 1
        
        return res