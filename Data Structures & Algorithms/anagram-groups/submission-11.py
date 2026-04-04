from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        """
        Input:
            A list of strings
        Output:
            A list of strings grouped by their anagram value
        Questions:
            How can I keep track of what items are an anagram?
            How to handle creating a new list, when I encounter a key I haven't seen
        Assumptions:
            I know an anagram has the same characters but in different order 
            So I can count the occurance of the key, and then use that key
            to store the anagram values
        Approach Idea:
            I could sort each item and use its sorted key for a dict, then store the values
            I could also create a list/tuple to store the key after
            I count the occurances of each value in the num

            Then I would check to see if the key is in the dict, if not
            add a new list to that key value
            if it is just appeand the value to the key
            then return a list containing the dict.values()

        Edge Cases:
            The string could be empty, or could be filled with white space?

    
        """

        char_store = defaultdict(list)


        for word in strs:
            storage_key = [0] * 26
            for char in word:
                storage_key[ord(char) - ord("a")] += 1
        
            char_store[tuple(storage_key)].append(word)
        return list(char_store.values())

        