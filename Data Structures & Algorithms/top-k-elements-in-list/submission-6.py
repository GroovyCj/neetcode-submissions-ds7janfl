
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: list of int
        # Output: a List containing top K elements
        """
        Approach:
        First count the frequency of the elements in the array
        Then group items based on how many times they appear:
        as such an element can only appear n times, which is the length of the array
        
        Then iterate through the frequency array, to pull off the top k elements
        
        
        """
        if len(nums) <= 1:
            return nums

        mp = {}
        for n in nums: # this will count the frequency of elements in the list
            mp[n] = 1 + mp.get(n, 0)
        
        freq = [[] for x in range(len(nums) + 1)]
        
        for key, v in mp.items():
            freq[v].append(key)
        
        result = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
        




        



    




      
     


    