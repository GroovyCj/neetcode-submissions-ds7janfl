class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):


            longest_odd = self.helper(s, i, i)
            longest_even = self.helper(s, i, i + 1)

            current_max = longest_odd if len(longest_odd) > len(longest_even) else longest_even
            if len(current_max) > len(res):
                res = current_max
        return res


    

    def helper(self, s, l, r):
        res_index, res_len= 0, 0
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_index = l
                    res_len = r - l + 1
                l -= 1
                r += 1
        return s[res_index:res_index + res_len]