class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input:
            list of nums, and a int target
        Output:
            The index of each num that fulfil the target in the array
            e.g. [0,1] or [2,3]
            earlier index has to appear first
        Assumptions:
            There is at least one correct answer for each  input
            the number we are looking for has to be target - current_num
            This will tell us what number we seen before + current_num will give us the target
            I must store the num and the index somewhere for later retrieval
        Approach Ideas:
            initialize a Dict

            loop through nums with index and value:
            target_num = target - current_num

            if target_num in dict:
                return [dict[target_num], index]
            dict[num] = index
        """


        seen: dict[int, int] = {}


        for index, num in enumerate(nums):
            target_num = target - num
            if target_num in seen:
                return [seen[target_num], index]
            seen[num] = index
        