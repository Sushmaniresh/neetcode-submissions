class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        best = 0
        for i in prices:
            cheapest = min(cheapest,i)
            best = max(best, i-cheapest)
            print(best)
        return best
        