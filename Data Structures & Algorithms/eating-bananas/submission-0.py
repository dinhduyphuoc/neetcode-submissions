class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            curRate = (l + r) // 2
            time = 0
            for pile in piles:
                time += (pile + curRate - 1) // curRate
            if time <= h:
                r = curRate - 1
            else:
                l = curRate + 1
        
        return l
