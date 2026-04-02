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
            counter = 0
            i = 0
            while num + i in nums:
                counter += 1
                i +=1
            longest = max(counter, longest)
        return longest












       



        
