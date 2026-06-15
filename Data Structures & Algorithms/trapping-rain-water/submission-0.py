class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = maxR = 0
        res = 0
        while l <= r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            wall = min(maxL, maxR)
            if height[l] < height[r]:
                res += wall - height[l]
                l += 1
            else:
                res += wall - height[r]
                r -= 1
        return res
        
