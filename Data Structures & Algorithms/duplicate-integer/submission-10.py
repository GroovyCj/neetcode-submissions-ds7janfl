class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        Input:
            A list of nums
        Output:
            Boolean value if a num appears more than once
        Questions:
            What is the best data structure to track duplicates
                Ideally something that has O(1) look up times
        Assumptions:
            I have to look at every number at least once
            I can exit early once I encountered a failure condition
        Approach idea:
            Initialize a set 
            check to see if num is in set
            if yes return True -> theres a duplicate
            if no, add it to the set
        Edge cases:
            what if the array is empty?
            What if the array only contains 1 element?


        Potential Bugs:
            Adding the number to the set, before doing the check
        """


        seen: set = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        