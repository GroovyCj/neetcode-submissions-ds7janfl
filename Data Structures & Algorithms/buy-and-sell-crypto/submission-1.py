class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        input: List of ints
        Output: Int, maximum proft I would receive that day
        constraints: Prices have to be higher than 1

        Approach:
        What would make the profit the highest:
            calculate profit, and keep the highest value
            Buying on a lower day, and selling at a higher:

        

        keep track of the highest profit

        highest profit day must be after the buy date
        
        
        
        """

        highest_profit = 0
        lowest_num = prices[0]

        for p in prices:

            lowest_num = min(p, lowest_num)

            curr_profit = p - lowest_num

            highest_profit = max(curr_profit, highest_profit)
        return highest_profit




        
            


    