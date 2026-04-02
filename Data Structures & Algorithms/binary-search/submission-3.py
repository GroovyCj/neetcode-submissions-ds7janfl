class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
            Input:
                A list of ints that is in sorted order, each item is unique i.e. no duplicates
            Output:
                A int value which is the index of the target input, or -1 if it can't be found
            Assumptions:
                input on left of the array is less than the input on the furthest right
                At the midpoint of the array
                    mid + 1 will be bigger than mid
                The target is in one half of the array or not at all
                    This is only true for sorted arrays
            Questions:
                How will I know that I hit my target input
                    What does the success criteria look like
                Being Binary Search, does this occur when the mid point is the target
            Approach Ideas:
                Initialize 2 pointers L and R
                loop through while L =< R
                See what half the target is in
                    if its in the right half i.e. target > mid drop the left half
                    other wise drop the right half
                Continue updating mid until it equals the target
        
        """

        l: int = 0
        r: int = len(nums) - 1


        while l <= r:
            mid: int = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1


      

 