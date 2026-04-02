class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input:
            Array of int that represent temperatures
        Output: 
            A array of ints, which represents the number of days until that day experinced warmer weather
                Return 0 for that day if there was no warmer day
        Questions:
            How do I keep track of the unresolved days?
            Can one day resolve multiple previous days?
            When do I add the current value
            How do I compute the number of days between curr day and the day it resolves
        Assumptions:
            There are going to be days that resolve multiple days
            I need to keep track of those days
            I need to keep track of the index of those days to compute number of days
        Approach-ideas:
            Create a stack to keep track of values

            Iterate through temperatures and see how many days the current value resolves, 
            Pop those values and compute the number of days difference
            add them to the res array

        
        
        """
        unresolved_temps = []
        res = [0] * len(temperatures)


        for i, temp in enumerate(temperatures):

            while unresolved_temps and temp > temperatures[unresolved_temps[-1]]:
                temp_idx = unresolved_temps.pop()
                res[temp_idx] = (i - temp_idx)
            unresolved_temps.append(i)
        return res

       