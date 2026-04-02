import re
pattern = r'[^a-zA-Z0-9]'

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s =  ''.join(x for x in s if x.isalnum()).strip().lower()

        new_s = []
        for x in s:
            if x.isalnum():
                new_s.append(x)
        s = "".join(new_s).strip().lower()

        L,R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
        return True 


     