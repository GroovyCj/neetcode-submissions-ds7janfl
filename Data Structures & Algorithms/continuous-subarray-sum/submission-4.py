class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        """
            Input:
                nums -> list of ints
                k -> The multiple the sum of nums must be
                    i.e. [2,4] sum to 6, if K is 6 its true as 6 * 1 = 6 
                    further multiple of 6 -> 6, 12, 18, 24, 30 etc...
            Output:
                Boolean -> if the sum of the subarray is a multiple of K
                    And there is atleast two inputs in that subarray
            Constraints:
                The subarray has to have at least two character
            Assumptions:
            Questions:
                How do I ensure the subarray has at least two characters
                    instead of prefilling the prefix, to account for the first input
                    I can leave it empty
                How can I find out if the sum is multiple of 6
                    I think if curr_sum modulo 6 == 0, its a multiple
                What does the prefix at i represent?
                what do I need to store in my prefix
            Approach Ideas:
                I know I need to keep track of the curr_sum
                I know I need to compute if that sum is a product of K
                I know I need to atleast go through each num once
                I know I can early exit if I get a truthy condition
        
        """

        curr_sum: int = 0
        prefix: dict = {0:-1}

        for i, num in enumerate(nums):
            curr_sum += num
            diff = curr_sum % k
            if diff in prefix and i - prefix[diff] >= 2:
                return True
            if diff not in prefix:
                prefix[diff] = i        
            
        return False

        