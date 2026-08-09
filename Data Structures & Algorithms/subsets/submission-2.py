class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, arr):
            res.append(arr.copy())
            if cur == len(nums):
                return
            for i in range(cur, len(nums)):
                arr.append(nums[i])
                dfs(i + 1, arr)
                arr.pop()
        
        dfs(0, [])
        return res