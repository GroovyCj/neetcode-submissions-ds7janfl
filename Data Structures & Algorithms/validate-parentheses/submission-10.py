class Solution:
    def isValid(self, s: str) -> bool:
     

     # Input: a string that contains characters
     # Output: Boolean
     # Assumptions: Every bracket is closed by the respetive close bracket [], {}, <>, () 
     # If a closing bracket is found, the respective opening bracket must have come before it 
     # Or the brackets were not closed in the correct order
     # EX {[{}]}, not [{]} as these are not closed correctly {{[}]}


     #Approach iteratively go through each entry in the string if we encounter a opening bracket store it,
     # if we encounter a closing bracket immediately compare it to the most previous opening bracket to see if it matches
        opening_brackets = []
        bracket_matches = {"]": "[", "}": "{", ")":"("}
        if len(s) <=1:
            return False

        for char in s:

            if char in bracket_matches:
                if opening_brackets == [] or bracket_matches[char] != opening_brackets.pop():
                    return False  
            else:
                opening_brackets.append(char)
        return opening_brackets == []

    

