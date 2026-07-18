class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i):
            res.append(cur.copy())
            for idx in range(i, len(nums)):
                cur.append(nums[idx])
                dfs(idx + 1)
                cur.pop()
        
        dfs(0)
        return res