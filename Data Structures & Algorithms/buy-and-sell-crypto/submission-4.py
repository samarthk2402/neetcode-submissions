class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0

        profit = 0
        maxp = 0

        for i in range(len(prices)):
            if prices[i] < prices[l]:
                profit = 0
                l = i
                r = i
            if prices[i] > prices[r]:
                r = i

            profit = prices[r] - prices[l]

            if profit > maxp:
                maxp = profit
                
        
        return maxp