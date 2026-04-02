class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #input: as a List where List[i] represents the temperature for that day
        #output: where List[I] is the number of days before a warmer temperature appears, if no warmer temperature appears set List[I] to 0
        # Assumptions: temperatures can be positive or negative, there could be no days were a warmer temperature is discovered


        res = [0 for i in range(len(temperatures))]
        stack = []


        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                last_idx = stack.pop()
                res[last_idx] = i - last_idx
            stack.append(i)
        return res








    
