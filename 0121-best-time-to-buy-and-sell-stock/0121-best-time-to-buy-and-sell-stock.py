class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = max(prices[right] - prices[left], profit)
            else:
                left = right
            right += 1
            

        return profit