from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] +=1
            ana[tuple(key)].append(word)
        return list(ana.values())




    