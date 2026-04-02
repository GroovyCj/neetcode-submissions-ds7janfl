from itertools import permutations 
from collections import deque

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Input: Two strings,
            Output: Boolean value, if the strings are permutations
            Permutations - One variation of a string exists in another
                Abc - cab, bac, bca, etc
            Constraints: all strings are lower case

            Approach Ideas:
                I know for a fact, the window size has to atleast be the size
                of the first string. 
                so the first window should start at 0, and end at index 2,
                then move the window over by one, until we find a match

                Each string can have up to 26 character as that is the english 
                alphabet, I can count the occurance by initializing the first 
                string using character placement ord(c) - ord(a), then place it in the 
                array
                for each window size check  to see if the character counts match if 
                it does its a permutation
        
        """


    
        L = 0
        R = len(s1) - 1
        if len(s1) > len(s2):
            return False
        s1_count = [0 for x in range(26)]
        s2_count = [0 for x in range(26)] 
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
            
        while R < len(s2):
            if s1_count == s2_count:
                return True
            
            s2_count[ord(s2[L]) - ord("a")] -= 1
            L += 1
            R += 1
            if R < len(s2):
                s2_count[ord(s2[R]) - ord("a")] += 1
        
        return False