class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)):
            if i >= 2:
                cost[i] += min(cost[i - 1], cost[i - 2])
        
        return min(cost[-1], cost[-2])