from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [1,2,3,4,5] a target
        index_holder = {} #key=num_value, dict_value=index


        for index, value in enumerate(nums):
            desired_num = target - value

            if desired_num in index_holder:
                return [index_holder.get(desired_num), index]
            index_holder[value] = index


        return []