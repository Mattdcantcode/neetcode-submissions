class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dif = []
        for i in range(n):
            m = max(prices[i:n])
            dif.append(m - prices[i])
        return max(dif)
