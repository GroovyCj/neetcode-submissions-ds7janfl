class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for k,v  in enumerate(nums):
            goal = target - v
            if goal in map:
                return [map[goal], k]
            map[v] = k

        