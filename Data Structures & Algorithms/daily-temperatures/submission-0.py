class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #input: as a List where List[i] represents the temperature for that day
        #output: List, where List[I] is the number of days before a warmer temperature appears, if not temperature appears set List[I] to 0
        # Assumptions: temperatures can be positive or negative, there could be no days were a warmer temperature is discovered


        res = [0] * len(temperatures)
        temps = []
      


        for i, t in enumerate(temperatures):
            while temps and t > temperatures[temps[-1]]:
                j = temps.pop()
                res[j] = i - j
            temps.append(i)
        return res
       
