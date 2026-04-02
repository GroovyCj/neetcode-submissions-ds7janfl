
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
            Input:
                String value 
            Output:
                int -> represents the longest substring without repeating characters
            Assumptions:
                This string can contain uppercase or lower case characters as there is no restrictions
                This is a sliding window problem
            Questions:
                When does the substring actually become invalid
                    When we encounter a duplicate character
                What do we do when the substring is invalids
                How do we keep track of the characters we have seen so far
                What is the proper datastructure to accomplish keeping track of the characters
                    I'm thinking a deque this will allow me to have constant time pops
      
            Approach Ideas:
            initialze two pointers L, R, deque, and a longest counter

            iterate from left to right
            add char to deque
            check for dups
            shrink window
            calculate longest the distance of the substring
            return longest value

        """
    
        l: int = 0
        longest: int = 0
        string_counter: dict = {}

        for r in range(len(s)): 
            if s[r] in string_counter:
                
                l = max(string_counter[s[r]] + 1, l)
            string_counter[s[r]] = r
            longest = max(longest, r - l  + 1)
        return longest

    

      
     
