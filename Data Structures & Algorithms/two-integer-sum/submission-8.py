
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #input: a list of ints
        #output: is going to be the indices of the two numbers that hit target
        # Need to go through each number atleast once, 
        # Need to also keep track of indices some how
        # calculate what the target num should be
        # Constraints: can have negative numbers,
        mp = {}


        for i, num in enumerate(nums):
            t  = target - num
            if t in mp:
                return [mp[t], i]
            mp[num] = i
        return []


