class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        currMin = prices[0]
        ret = 0

        for p in prices:
            currMin = min(currMin, p)
            ret = max(ret, p - currMin)

        return ret