class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        res = 0

        for sell in range(len(prices)):
            res = max(res, prices[sell] - bestBuy)
            bestBuy = min(bestBuy, prices[sell])

        return res