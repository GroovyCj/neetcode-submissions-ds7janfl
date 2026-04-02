from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for word in strs:
            key = sorted(word)
            ana[tuple(key)].append(word)
        return list(ana.values())




    