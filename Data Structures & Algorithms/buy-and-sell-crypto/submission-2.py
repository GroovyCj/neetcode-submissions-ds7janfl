class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input:
            A list of prices which is a list of ints
        Output:
            a Int value that represents the highest profit I could get
        Assumptions:
            I would have to buy on the lowest day and sell on the highest day after that lowest day
            I.e. I can't jump to an index that is before the index of the price I am at
        Questions:

        Approach Ideas:
            Need to initlize a variable to store the lowest price
            I need store the highest_profit

            Loop through each item, 
                Readjust the lower price, 
                The compare lowest price to current price
                then update max_profit, 
                once done
                return max_profit

      
      
      

      """

        lowest_p: int = prices[0]
        max_profit: int = 0


        for num in prices:
            lowest_p = min(lowest_p, num)
            curr_profit = num - lowest_p

            max_profit = max(curr_profit, max_profit)
        return max_profit