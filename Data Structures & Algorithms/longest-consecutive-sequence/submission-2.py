class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Input: List of ints
        Output: Int length of longest consecutive sequence

        Assumptions: Original array order doesn't matter
        Output array: can pull consecutive numbers from original array

        Need to count longest sequence
        Need a way to track sequences   
        """

        nums = set(nums)
        longest = 0

        for num in nums:
           
            if num-1 in nums:
                continue
        
            i = 0
            while num + i in nums:
             
                i +=1
            longest = max(i, longest)
        return longest












       



        
