import re
pattern = r'[^a-zA-Z0-9]'

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  ''.join(char for char in s if char.isalnum()).strip().lower()
        L = 0
        R = len(s) -1
        while L < R:
            if s[L] != s[R]:
                return False
            L = L + 1
            R = R - 1
        return True
        