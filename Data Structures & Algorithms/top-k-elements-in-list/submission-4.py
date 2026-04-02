from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      """
      input:
      Int Array: the numbers
      int k: num of items we want returned

      output:
      array: top K elements, for example top 3 elements
      in any order

      Assumptions:
      Can return the array an any order
      There are no negative numbers

      Approach:
      Loop through the array to count the occurances of the items in the list

      {5:2, 1:1, 2:3}


      make an array that uses the value from the dictionary as the insertion point

      
      
      
      
      
      
      """



      if len(nums) == 0:
        return []
      if len(nums) == 1:
        return nums
      
      freq = [[] for _ in range(len(nums) + 1)]

      mp = {}
      for num in nums:
        mp[num] = 1 + mp.get(num, 0)
      


      
    

      for key, cnt in mp.items():
        freq[cnt].append(key)
    

      res = []
      for i in range(len(freq) -1, 0, -1):
        for item in freq[i]:
          res.append(item)
        
          if len(res) == k:
            return res


    
      return []


      
     


    