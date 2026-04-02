class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            Input: list of ints, in a semi-sorted rotated array
            Output:  index of the target, or -1 if not found

            Questions:
                How do I know what side of the array is sorted,
                    For example where exactly is the pivot point
                When I am in the sorted side, what do I do,
                    Check to see if the target is in that side, How?

            Assumptions:
                There has to be at least one side of the array that is still sorted, either left or right
                The value could be in one side, either left or right or not at all

            Approach: 
                Create three pointers
                    L
                    R
                    M
                Run a while loop (L<=R)
                Check to see what side of the array is sorted:
                    Left:
                        See if the Target is in the side
                            Yes:
                                Run Loop to iterative eliminate portions
                            No:
                                Must be in Right side
                                Move pointers to work in the right side
                    Right:
                        Opposite of left
                Not found in Either?:
                    Return -1
        
        """


        L = 0
        R = len(nums) -1 # -1 to account for the index

        while L <= R:
            mid = L + (R-L) // 2
            if nums[mid] == target:
                return mid

            if nums[L] <= nums[mid]: # means left side is sorted
                if target > nums[mid] or target < nums[L]:
                    # This means the target is not in this side
                    L = mid + 1
                else:
                    R = mid - 1
            else: # right side is sorted

                if target < nums[mid] or target > nums[R]:
                    # target is not in right side
                    R = mid - 1
                else:
                    L = mid + 1
        return -1
            
        
