from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [1,2,3,4,5] a target
        mydict = dict()


        for index, value in enumerate(nums):
            desired_num = target - value;
            if desired_num in mydict:
                 return [mydict[desired_num], index] 
            mydict[value] = index  
          
        