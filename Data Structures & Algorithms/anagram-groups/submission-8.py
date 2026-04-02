from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Input:
            A list of strings
        Output:
            A list of lists that contains strings
                Each one of these sublist represent inputs that are anagrams of eachother
        Assumptions:
            A sublist can contain one or many inputs
            Anagrams have the same exact characers just in different order
                e.g. cat and act, -> same exact character just in different order
            I could sort the value, but that would make this an N log n solutionj
            I could also make a new key for each character by counting the occuranc
        Questions:
            How do I know when to append the character to a certain list
                What value can I use as an indicator that it belongs to a certain sublist
        Approach Ideas: 
            I could sort the value, but that would make this an N log n solutionj
            I could also make a new key for each character by counting the occuranc

            Create a res list to contain all the sublist
            get a new num, sort it
                check to see if sorted key exist in res
                if not add a new sublist, 
                else append the curent value to that sublist

             
        """

        res: dict = {}
        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord("a")] += 1
            key = tuple(key)
            if key not in res:
                res[key] = []
            res[key].append(s)
        return [x for x in res.values()]
      