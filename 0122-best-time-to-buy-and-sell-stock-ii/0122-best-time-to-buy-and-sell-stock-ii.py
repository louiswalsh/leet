class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, minPrice = 0, 99999999999999999999999999999

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])

            if prices[i] - minPrice > 0:
                profit += prices[i] - minPrice
                minPrice = prices[i]


        
        return profit