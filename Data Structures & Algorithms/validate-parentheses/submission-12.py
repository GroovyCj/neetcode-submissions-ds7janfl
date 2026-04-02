from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        """
        Input: a str that contains bracket characters {}()<>[]
        Output: Bool value, if the brackets are closed in the correct order
        Questions:
            When does the string stop being valid, i.e. when is the fail condition
                must be closed by same bracket
                must be in correct order
                ever closing bracket must have a opening bracket
            What data structure makes this the easiest
                A stack for popping the most recent value
                A deque has same benefit of the stack just a little faster
        Assumptions
            Opening brackets could not have a closing bracket
            Closing brack could not 
            I must go through each character in the sequence failing early if there is a mismatch
        Approach Idea: 
            create a key value list to keep track of what closing bracket corresponds to an opening bracket
            Create a stack strucure to keep track of all the opening brackets in the str
            When we encounter a closing bracket, pop the most recent opening brack from the stack to see if they match
            if they do, keep going,
            else early exit with a false as no other values will make this correct
            if its an opening bracket append it to the stack

            if we make it through with no early exit,
            return True


        """

        bracket_pairs = {"]":"[", "}":"{", ")":"("}
        bracket_stack = deque()
       

        for char in s:
            if char in bracket_pairs:
                if not bracket_stack or bracket_stack.pop() != bracket_pairs[char]:
                    return False
            else:
                bracket_stack.append(char)
        return not bracket_stack



