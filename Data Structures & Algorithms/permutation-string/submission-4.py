

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Input:
                s1, s2 -> two string values 
            Output:
                Boolean, if s2 contains a permutation of the s1
                    -> this means that s1 is contained inside s2 but maybe in a different form
                        -> abc,  bac, cab, etc
            Assumptions:
                This is a sliding window problem.
                I have to check each value at least once
                if the two strings are permutations that means they have the same exact characters
                    abc -> bac are permutations
                The window for the sliding window has to be the len(s1)
                    Nothing else would make sense
                we can early exit if s1 is longer than s2, cause they can't be permutations 
            Questions:
                How do I keep track if the characters are the same?
                When is the window invalid?
                    the window stays invalid as long as the characters do not match
                When is the window valid?
                    when the character counts for each window match
            Approach Ideas:

                if len(s1) > len(s2):
                    return False
                I think I need to count the freq of each character
                each string needs there own frequency counter
                Then we can prefil each counter to the length of s1
                    Window has to atleast be the size of s1
                check to for validity as the first prefil could be the answer
                we loop through each character in s2 starting where we ended the prefil
                add its count to s2
                if its valid we return true
                if not we remove the character from the s2 count
                if we get to the end of the loop with no early True, return False

        """
        if len(s1) > len(s2):
            return False

        l: int = 0
        k: int = len(s1)


        s2_count: int = [0] * 26
        s1_count: int = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] +=1
            s2_count[ord(s2[i]) - ord("a")] +=1

        if s1_count == s2_count:
            return True

        for r in range(k, len(s2)):
            s2_count[ord(s2[r]) - ord("a")] += 1
            s2_count[ord(s2[l]) - ord("a")] -= 1
            l += 1

            if s1_count == s2_count:
                return True
        return False




        


    
     
        