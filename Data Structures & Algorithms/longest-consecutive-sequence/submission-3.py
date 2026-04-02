class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Input: List of ints
        Output: Int length of longest consecutive sequence

        Assumptions: Original array order doesn't matter
        Output array: can pull consecutive numbers from original array

        Need to count longest sequence
        Need a way to track sequences 
        How do I know if a number is the start of a sequence,
        How do I know if a number is the end of a sequence 
        I need to have O(1) Look up time to prevent O(n) lookup
        Dict checking for keys is O(1)
        Set checking for keys in O(1)


        Apprach:

        I need   
        """
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            i = 1
            while num + i in nums:
                i += 1
            longest = max(i, longest)
        return longest
            



     












       



        
