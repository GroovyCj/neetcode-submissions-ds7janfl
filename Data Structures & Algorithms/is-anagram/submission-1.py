class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        if sorted(sl) == sorted(tl):
            return True
        else:
            return False
      


        