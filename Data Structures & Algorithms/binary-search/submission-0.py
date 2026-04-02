class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Array low -> high, Ascends
        # -9999 to -9999
        # all nums are unique, no repeats
        low = 0
        high = len(nums) -1
     
        
        while low <= high:
            mid = int( high + low / 2)

            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid -1
            else:
                return mid
        return -1

