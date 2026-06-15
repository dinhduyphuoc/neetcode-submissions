class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) 
        i = 0
        while i < k:
            if nums[i] == val:
                l = i
                r = i + 1
                while r < k:
                    nums[l] = nums[r]
                    l += 1
                    r += 1
                k -= 1
            else:
                i += 1
        return k
