class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                arr.append(candidates[i])
                backtrack(i + 1, total + candidates[i], arr)
                arr.pop()
            
        backtrack(0, 0, [])
        return res