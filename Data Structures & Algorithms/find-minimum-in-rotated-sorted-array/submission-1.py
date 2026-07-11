class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            pivot = (l + r) // 2
            if nums[pivot] > nums[r]:
                l = pivot + 1
            else:
                r = pivot
        return nums[l]