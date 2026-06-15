class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [nums[0]] * len(nums)
        left = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            right[i] = nums[i] * right[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            left[i] = nums[i] * left[i + 1]
        
        nums[0] = left[1]
        nums[-1] = right[-2]

        for i in range(1, len(nums) - 1):
            nums[i] = left[i + 1] * right[i - 1]
        
        return nums