class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """

        Input: a List of nums, which represents a sorted array of ints
            target: a int value which is the number we want to find in the sorted array
        Output: 
            The index of the target in the sorted array or -1 if the item cannot be found
        Questions:

        Assumptions:
            The List can contain negative numbers
            The list is sorted so the smallest number is on the left,
            Largest is on the right

            Searching normally would be an O of N solution 
            We can  use the ascending order to our benefit
            By Checking which half of the list the target exists in based on a pivot point

        Approach:
            Initialize three pointers, one at the beginning one at the end, and one in the  middle
            Check if the target is bigger or smaller than the middle pointer
            if the target is smaller the target could be in the left half
            if the target is bigger the target could be in the right half
            if the target is the middle number return its index

        
        
        
        
        
        
        
        
        
        """


        L = 0
        R = len(nums) - 1 # we do -1 to account for the index, i.e. if the len is 8, the index of the last num is 7

        # [-1,0,2,4,6,8] t =0
        while L <= R:
            mid = R + L // 2
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                R = mid - 1
            if target > nums[mid]:
                L = mid + 1
        return -1






 