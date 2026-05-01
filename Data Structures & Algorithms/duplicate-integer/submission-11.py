class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        Input:
            A list of int values,
        Output:
            Boolean value if the item was seen before
        Assumptions:
            worst case there are no duplicates and we have to check each number at least once
                Then return False
            we can early exit soon as we see a duplicate
            We are going to assume the array can be empty
        Questions:

        Approach Ideas:
            I can have a set for to capture seen elements:
            As I go through the array add element to seen after checking
            This allow O(1) look up time
                and O(n) Auxiliary space

        
        """


      
        
        seen: set[int] = set()
        # Python wont execute the loop at all if the empty is empty
        for n in nums:
            if isinstance(n, int):

                if n in seen:
                    return True
                
                seen.add(n)
            else:
                return False

        return False 
