class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i,n in enumerate(prices):
            if n<min_price:
                min_price = n
            else: 
                res = max(res, n-min_price)
        return res
        