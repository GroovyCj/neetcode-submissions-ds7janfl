class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana = {}

        if not strs:
            return [[""]]


        for word in strs:
            key = "".join(sorted(word))
            if key in ana:
                ana[key].append(word)
            else:
                ana[key] = [word]
            
        return list(ana.values())