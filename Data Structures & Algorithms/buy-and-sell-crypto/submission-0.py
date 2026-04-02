class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_seen = 0
        min_price_seen = prices[0]

        #  [10,1,5,6,7,1]

        for todays_price in prices:
            todays_profit = (todays_price - min_price_seen)
            
            max_profit_seen = todays_profit  if todays_profit > max_profit_seen else max_profit_seen
        
            if todays_price < min_price_seen:
                min_price_seen = todays_price
        
        return max_profit_seen


            


    