class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for char in s:
            if char in map_s:
                map_s[char] +=1
            else:
                map_s[char] = 1
        
        for char in t:
            if char in map_t:
                map_t[char] +=1
            else:
                map_t[char] = 1


        return map_t == map_s


        