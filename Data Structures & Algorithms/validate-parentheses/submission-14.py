class Solution:
    def isValid(self, s: str) -> bool:
        """
            Input:
                Str containing brackets
            Output:
                Boolean if all brackets are closed in the proper order
            Assumptions:
                If any of the brackets are out of order I can fail immediately
                Not every bracket will have a closing bracket
            Approach Ideas:
                1. Create data structures to store brackets
                2. Create a key to map valid inputs
                3. loop through each character
                4. Store opening bracket or validate closing bracket
                5. Fail early on mismatch, or return True if loop completes

        """

        opening_brackets: list[str] = []
        bracket_map: dict[str, str] = {"]":"[", "}":"{", ")":"("}


        for char in s:

            if char in bracket_map:
                if not opening_brackets or opening_brackets.pop() != bracket_map[char]:
                    return False
            else:
                opening_brackets.append(char)
        return not opening_brackets

                


        