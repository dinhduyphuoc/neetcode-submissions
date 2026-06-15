class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0
        for num in nums:
            if num == majority:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    majority = num
                    count = 0
        
        return majority