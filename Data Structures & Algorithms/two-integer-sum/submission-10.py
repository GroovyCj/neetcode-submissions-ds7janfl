
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input:
            List of ints, bet can be negative or positive

            Target -> a number that two indices sum to
                nums[i] + nums[j] = target
        Output:
            A list containing the indices of the two numbers
                The first item in the list should be the earliest encountered index
        Questions:
            How do I keep track of what indices I encountered
            How do I populate the list when I find them
        Assumption:
            I have to keep track of the index at some point as I have to 
            return it
            I have to compute the desired num -> targeted - nums[i]
                This is the number to check to see if I encountered it
        Approach Ideas:
            a Dict would be a good data structure to keep track of the nums
            and its index
            loop through nums
                calculate the diff, check to see if diff in dict
            if it is return indexes
            if not add num to dict
            if I don't find it return false
        
        """

        seen: dict = {}

        for idx, num in enumerate(nums):
            desired_num = target - num
            if desired_num in seen:
                return [seen[desired_num], idx]
            seen[num] = idx
        
    

     