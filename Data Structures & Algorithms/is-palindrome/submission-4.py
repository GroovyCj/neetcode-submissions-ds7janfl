

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
    # Input:  A string
    # Output: Boolean value
    # Assumptions: String can contain non alphanumeric characters

    # Approach: first we need to sanitize the string, as it could contian whitespace or characters we dont need
    # Restrict to only alphanumeric characters
    # Then we can initialize two pointers and iteratively compare the first string to the last string and move the pointers
    # if at any point the characters aren't the same we know its not a palindrome early exit


        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1

            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1

        return True