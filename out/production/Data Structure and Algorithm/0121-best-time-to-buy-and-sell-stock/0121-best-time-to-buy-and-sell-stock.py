class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum = 0
        # i, j = 0, 1

        # while j < len(prices):
        #     if prices[i] < prices[j]:
        #         maximum = max(maximum, prices[j] - prices[i])
        #     else:
        #         i = j      # update the buying day
        #     j += 1

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit