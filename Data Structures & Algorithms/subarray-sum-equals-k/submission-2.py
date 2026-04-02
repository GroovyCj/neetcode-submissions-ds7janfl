from collections import deque


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:



        # Input: array of int, and and K the target we are hitting
        # Output: is an int that represents the number of subarrays that hit the target
        # Assumptions: Values can be positive or negative 
        # an item by itself can hit the sum: for example K = 4, and [4,4,4 ] means 3 targets hit the sum
        """

        i need to keep track of the amount of hits
        Need to keep track of the current sum
        need to keep track of a prefix sum   
        
        """

        hits = 0
        cur_sum = 0
        prefix_sum = {0: 1}
        for num in nums:
            cur_sum += num
            desired_num = cur_sum - k
            if desired_num in prefix_sum:
                hits += prefix_sum.get(desired_num)
            
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        return hits







        