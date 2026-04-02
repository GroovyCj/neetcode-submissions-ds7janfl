
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
            Input:
                a list of nums
                target, int the number we are trying to sum to
            Output:
                is going to be the indices of the two numbers
            Assumptions:
                The numbers can be negative,
                Cannot use the same number twice
                There is only one true answer for each questions
            Questions:
                How do I keep track of the indices of the problem
                    I think I should use a dictionary to store indices so I can retrive it later
            Approach Ideas:
                Initialize a dictionary to store values and indices
                loop through nums
                compute the number we need,
                check to see if its in the set:
                add current number and indices to set
        
        
        
        
        """
        seen: dict = {}

        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in seen:
                return [seen[needed_num], i]
            seen[num] = i
        