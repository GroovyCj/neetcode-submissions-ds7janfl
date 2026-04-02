class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            Input: a List of nums that has been rotated
            Output:
                The minimum number in an array
            Assumptions:
                if the array is truly rotated, the minimum number will always
                be after the pivot point
                One half of the array should be sorted in
                    i.e. input on left is smaller than input on right i.e. L < M, or M < R
                Numbers can be negative
                if the left pointer is smaller than the right pointer at onset it means the array is sorted already
            Questions:
                How do I figure out what side is sorted,
                    once I figure this out whats next
                    Start exploring that side of the input
            Approach Ideas:
                I think if one side is sorted, the other side will contain the pivot point
                once I find the pivot point I can move my pointers to that side

                Have a L and Right pointer
                Check to see if L < R
                    if so the array is already sorted
                    return array at left pointer
                then while L <=R
                    get mid point
                check to see what side is sorted
                    if left side is sorted
                        move L to mid plus !
                    else:
                        move R to mid
                The left pointer should eventually hit the lowest point



        """

        l: int = 0
        r: int = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l] # Array is already sorted

        while l < r:
            mid = l + ((r - l) // 2)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
    