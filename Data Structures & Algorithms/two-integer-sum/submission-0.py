class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            minus = target - nums[i]
            if minus in check:
                return [check[minus], i]
            check[nums[i]] = i