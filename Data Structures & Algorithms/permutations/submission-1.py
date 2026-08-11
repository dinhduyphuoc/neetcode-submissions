class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, visited, arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for i in range(cur, len(nums)):
                if nums[i] in visited:
                    continue
                arr.append(nums[i])
                visited.add(nums[i])
                dfs(cur, visited, arr)
                arr.pop()
                visited.remove(nums[i])

        dfs(0, set(), [])
        return res