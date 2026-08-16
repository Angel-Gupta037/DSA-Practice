class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        n=len(prices)
        m=len(discounts)
        total=0
        for i in range(n):
            if i<m:
                total += prices[i] * (100 - discounts[i]) / 100
            else:
                total += prices[i]
        return total