class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr, visited):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for i in range(len(nums)):
                if i in visited:
                    continue 
                visited.add(i)
                arr.append(nums[i])
                backtrack(arr, visited)
                visited.remove(i)
                arr.pop()

        backtrack([], set())
        return res
            