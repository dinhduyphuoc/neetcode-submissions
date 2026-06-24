class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        l = 0
        def append(i):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
        for r in range(len(nums)):
            append(r)
            if r - l + 1 > k:
                l += 1
            if window and window[0] < l:
                window.popleft()
            if r - l + 1 == k:
                res.append(nums[window[0]])
        
        return res




