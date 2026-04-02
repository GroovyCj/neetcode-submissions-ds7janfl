class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #input: list that contains [start, end]
        #output:  A list of intervals where no points overlaps [[1, 2], [2,3] -> [[1,3]] as both have the same start and end point
        # Assumption that the list is in some type of order -> ascending



        
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]


        for start, end in intervals:
            if start <= ans[-1][-1]:
                ans[-1][-1] = max(ans[-1][-1], end)
            else:
                ans.append([start,end])
        return ans





        