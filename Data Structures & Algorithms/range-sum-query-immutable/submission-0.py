class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix: list = []
        total: int = 0
        for num in nums:
            total += num
            self.prefix.append(total)
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]

       
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


"""
    Input:
        List of ints -> that represent a array of nums
    Output:
        for the sumRange function, when given two points I return the sum between those two indices
    Assumptions:
        Numbers can be negative,
        return value can be positive or negative
        at most I will always get two points






"""