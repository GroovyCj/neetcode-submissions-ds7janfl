class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Input: str 
        # Output: int, longest substring value, with no repeating characters
        #assumptions: Can have repeated characters, there are no empty spaces, 


        # keep track we seen the character some how
        # we need to calculate ands track the longest substring
        # we need to keep track on how we are moving through the string
        # Sliding window: we need to resize window when a duplicate chracter is found
        # Sliding windows move iteratively, removing characters until the issue is resolved

        L = 0
        max_seen = 0
        seen = set()


        for R in range(len(s)):

            while s[R] in seen:
                seen.remove(s[L])
                L +=1
            seen.add(s[R])
            max_seen = max(max_seen, len(seen))
        return max_seen
