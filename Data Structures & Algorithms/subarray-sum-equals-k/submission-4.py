
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
        Input:
            List of nums
            K -> a target in which a sublist of nums sum to
        Output:
            The total number of subarrays that sum to the target
        Assumptions:
            The array can have negative numbers
            The array can be populated with 0s
            The first input in the subarray can be the target num
                i.e. a subarray can be a singular int
            Must keep track of the running sum
            must keep track of the differences between the current sum, and the target
                i.e. curr - k = diff -> must keep track of this somehow
        Questions:
            What is the proper way the keep track of the current sums?
                A variable?
            if we store the prefix, what exactly does it represent at any given moment?
        Approach ideas:
            Initilize a curr_sum variable
            initialize a prefix dictionary
            loop through nums:
            add it to running sum
            compute difference between running sum and K
            if we've seen it before update res variable?
            add currsum to prefix dictionary
        
        """

        curr_sum: int = 0
        prefix: dict = {0:1}
        res: int = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix.get(diff, 0)
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)
        return res

        
            
           




  