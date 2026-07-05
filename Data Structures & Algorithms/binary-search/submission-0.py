class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return -1