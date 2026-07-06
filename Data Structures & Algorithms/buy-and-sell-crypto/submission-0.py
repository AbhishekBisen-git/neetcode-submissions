class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = prices[0]
        diff = 0

        for i in range(len(prices)):
            if prices[i] - lp<0:
                lp = hp = prices[i]
            elif prices[i]-lp>diff:
                hp = prices[i]
                diff = hp - lp
        return diff