class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Input: Array, thats sorted in non-descending order [1,1,2,3,3,4]
        #Output: indices of two number that equal the sum target = 4, [2,2,3,4,6] return [0,1] and index 1 < index 2
        #constraits: indices cannot be equal, cannot use same element twice, Must be O(1)
        #assumptions: can include negative numbers


        L, R = 0, len(numbers) - 1


        while L < R:
            cur_sum = numbers[L] + numbers[R]

            if cur_sum > target:
                R-=1
            elif cur_sum < target:
                L +=1
            else:
                return [L+1, R+1]
           
        return []

        

