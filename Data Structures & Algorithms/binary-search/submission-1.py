class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Array low -> high, Ascends
        # -9999 to -9999
        # all nums are unique, no repeats

        #output: single int, that represents the target number index, or negative -1 if not found
        # What does the output depend on? no direct dependencies 
        # What must survive at I, we have to keep track of where we are at in the array, left side, right side, or middle
        # The array is in ascending order, so we know everything to the left is smaller and to the right is bigger
        # the out put doesn't have to be ordered as it is a single target


        L = 0
        R = len(nums) - 1
     

        while L <= R:
            Mid = (R + L) //2
            if nums[Mid] == target:
                return Mid
            if target > nums[Mid]:
                L = Mid + 1
            if target < nums[Mid]:
                R = Mid - 1
        return -1

