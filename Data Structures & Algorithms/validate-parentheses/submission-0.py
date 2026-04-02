class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []
        valid_pairs = ["[]", "{}", "()"]
        
        for char in s:
            if char == "[" or char == "{" or char == "(":
                valid_stack.append(char)
            else:
                if not valid_stack:
                    return False
                if valid_stack.pop() + char not in valid_pairs:
                    return False

        return not valid_stack

           
             
          

        

        