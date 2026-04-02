class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       map = {}
       for j, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [map[diff], j]
        map[n] = j
        