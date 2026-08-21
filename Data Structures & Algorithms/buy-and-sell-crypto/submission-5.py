class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i,n in enumerate(prices):
            min_price = min(min_price,n)
            res = max(res, n-min_price)
            print(min_price, res)
        return res
        