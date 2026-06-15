class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = 0
        res = [0] * len(arr)
        for i in range(len(arr)):
            if i == len(arr) - 1:
                res[i] = -1
            else:
                res[k] = max(arr[i + 1:])
                k += 1
        return res