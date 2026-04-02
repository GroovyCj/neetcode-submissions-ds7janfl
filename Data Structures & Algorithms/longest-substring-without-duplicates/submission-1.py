class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Input: str 
        # Output: int, longest substring value, with no repeating characters
        #assumptions: Can have repeated characters, there are no empty spaces, 



        L, longest_length = 0, 0
        seen = set()
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L +=1
            seen.add(s[R])
            longest_length = max(longest_length, len(seen))
        return longest_length


