

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
    # Input:  A string
    # Output: Boolean value
    # Assumptions: String can contain non alphanumeric characters

    # Approach: first we need to sanitize the string, as it could contian whitespace or characters we dont need
    # Restrict to only alphanumeric characters
    # Then we can initialize two pointers and iteratively compare the first string to the last string and move the pointers
    # if at any point the characters aren't the same we know its not a palindrome early exit


        new_string = []

        for i in s:
            if i.isalnum():
                new_string.append(i)
        s = "".join(new_string).strip().lower()
    

        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
