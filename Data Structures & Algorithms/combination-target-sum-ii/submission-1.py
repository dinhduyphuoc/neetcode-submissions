class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(cur, total, arr):
            if total > target:
                return
            if total == target:
                res.append(arr.copy())
                return
            for i in range(cur, len(candidates)):
                if i > cur and candidates[i] == candidates[i - 1] and i:
                    continue
                arr.append(candidates[i])
                dfs(i + 1, total + candidates[i], arr)
                arr.pop()
            
        dfs(0, 0, [])

        return res