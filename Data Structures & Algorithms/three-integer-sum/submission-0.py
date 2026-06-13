class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            mid = i + 1
            r = len(nums) - 1

            while mid < r:
                curSum = nums[i] + nums[mid] + nums[r]
                if curSum == 0:
                    res.append([nums[i], nums[mid], nums[r]]) 
                    while mid < r and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < r and nums[r] == nums[r - 1]:
                        r -= 1
                    mid += 1
                    r -= 1
                elif curSum > 0:
                    r -= 1
                else:
                    mid += 1

        return res
