class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curSum, arr):
            if curSum == target:
                res.append(arr.copy())
                return
            if curSum > target:
                return
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                curSum += nums[i]
                backtrack(i, curSum, arr)
                curSum -= arr.pop()

        backtrack(0, 0, [])
        return res