
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
            Input: 
                list of ints, positive or negative
                K -> a sum target we watch to reach
                
            Output:
                The number of sublist that hit the int target K
            Assumptions:
                I have a sublist so I must keep track of the array at certain points
                I have to keep track of the sum in some capacity for those givin points
                I must keep track of the amount of subarray sums that equal K
                I don't have to store those sums in any index e.g. another array
                The first item in the array can equal the sum
            Questions:
                What if the first item in the array equals that sum? how do I account for that
                If this is a prefix sum problem, what exactly does that sum represent at any given point
                What do I do with the sum once I have it?
                Can I use the sum as is? or is it a representative value?

            Approach Ideas:
                Initialize a current sum
                initialize a res value to account for hits
                initialize a prefix sum datastructure
                    prefil the datastructure with the first entry
                    this acounts for if the target is the first item
                loop through each value in the nums array
                    add it to the current sum
                    compute the difference beteen the sum and the array, check to see
                    if we seen it and add it to the resolt
                    add it to prefix sums
                return result

     
        """

        res: int = 0
        cur_sum: int = 0
        prefix: dict = {0:1}

        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            res += prefix.get(diff, 0)
            prefix[cur_sum] = 1 + prefix.get(cur_sum, 0)
        return res


           
            
           




  