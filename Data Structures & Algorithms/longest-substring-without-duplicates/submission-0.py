class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, longest_seen = 0,0
        mp = {}




        for R in range(len(s)):

            if s[R] in mp:
                L = max(mp[s[R]] + 1, L)
            mp[s[R]] = R

            longest_seen = max(R-L +1, longest_seen)
        return longest_seen

