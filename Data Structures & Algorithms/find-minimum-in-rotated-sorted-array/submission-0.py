class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Input: a Rotated sorted Array(list)
        Output: int, the minimum value in the sorted array
        Questions:
            How do I know when I have found the minimum value?
                How do I keep track of the minimum value?
            How do I know which side is sorted?
            if one sided is sorted does that mean the lowest value is in the unsorted side
        Assumptions:
            Each value is unique (No duplicates)
            if one side is sorted, The lowest number has to be move past the highest point
        Approach: 
            Set up 3 pointers
                left
                right 
                middle
            
            Then loop through while L < R
            [4,5,0,1,2,3]
                 L R
            [3,4,5,0,1,2]
            [2,3,4,5,0,1]
            [5,0,1,2,3,4]
        """

        L = 0
        R = len(nums) - 1

        while L < R:
            mid = L + ((R - L) // 2)
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[L]

 

        