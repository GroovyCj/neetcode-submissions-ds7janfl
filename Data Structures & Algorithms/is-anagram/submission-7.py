class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        input:
            Two string values
        Output:
            Bool if the one strin is an angram of another
        Assumptions:
            One string could be smaller than the other
            if the characters counts are different they are not anagrams
                E.g. one has 3 A's and the other has 1 A
            If I loop through we can exit the function early if something isn't the same
        Approach Ideas:
            First check if the len of both strings are the same
                mismatch -> fail early

            Idea # 1
            I could sort them and check for equivalency
            Thats an nLog N + mlog N solution (Sorting Both Strings)

            Idea # 2
            Create two lists, from 0 to 26
            Fill in both lists the the occurancies of each char
            compare two list for equivalency 

        
        
        
        """
        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for i in range(len(s)):
            count_s[ord(s[i]) - ord("a")] += 1
            count_t[ord(t[i]) - ord("a")] += 1
        return count_s == count_t




        