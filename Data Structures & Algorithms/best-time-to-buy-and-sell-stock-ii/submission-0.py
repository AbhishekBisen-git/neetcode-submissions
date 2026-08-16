class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices = prices
        d = {}
        profit = 0


        for right in range(len(prices)):
    
   
            d[right] = prices[right]
            print(right)
            if d and right>0 and d[right]>d[right-1]:
                val = prices[right] - prices[right-1]
                #print(prices[right],prices[right-1])
                #print(val)
                profit+= val
        
        return profit