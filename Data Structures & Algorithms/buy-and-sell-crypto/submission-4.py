class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i,n in enumerate(prices):
            res = max(res, max(prices[i:])-n)
        return res
        