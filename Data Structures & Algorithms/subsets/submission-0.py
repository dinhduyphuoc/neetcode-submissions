class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(start):
            res.append(cur.copy())
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
        dfs(0)
        return res
