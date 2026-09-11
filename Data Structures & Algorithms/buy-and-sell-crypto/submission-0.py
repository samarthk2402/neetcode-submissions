class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running = 0
        profit = 0
        for i in range(len(prices)-1):
            change = prices[i+1] - prices[i]
            if change >= 0:
                running += change
            else:
                if running + change > 0:
                    running += change
                else:
                    running = 0

            if running > profit:
                profit = running

        return profit
