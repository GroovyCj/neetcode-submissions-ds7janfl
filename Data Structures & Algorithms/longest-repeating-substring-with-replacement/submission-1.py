from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input:
            s - string of uppercase characters
            k - int value representing number of character edits allowed
        Output: 
            int maximum value of same characters we can get with the allow edits

        Constraints:
            K
                can have 0- len(s) edits
            S
                can be 1-1000 characters
        Questions:
            When do we move the window what makes the window valid?
                Each character has to get checked at least once, so we must move the window iteratively
            When do we shrink the window i.e. what makes the window invalid?
                The window becomes invalid when we run out of K edits
            How do we incorporate the K amount of edits?
        Assumptions:
            Within a Window we want to know what character appears the most
            From there we can decide how many edits to make to get the longest string

            We must keep track of what the longest string looks like at each step

      

        
        """

        L = 0
        count = Counter()
        max_freq = 0
        longest = 0

        for R in range(len(s)):
            count[s[R]] +=1
            max_freq = max(max_freq, count[s[R]])

            while (R - L + 1) - max_freq > k:
                count[s[L]]-=1
                L +=1
            longest = max(longest, R - L + 1)
        return longest


            


