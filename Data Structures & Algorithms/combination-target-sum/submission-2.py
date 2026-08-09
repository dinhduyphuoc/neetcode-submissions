class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, total, arr):
            if total > target:
                return
            if total == target:
                res.append(arr.copy())
                return
            for i in range(cur, len(nums)):
                arr.append(nums[i])
                dfs(i, total + nums[i], arr)
                arr.pop()

        dfs(0, 0, [])

        return res