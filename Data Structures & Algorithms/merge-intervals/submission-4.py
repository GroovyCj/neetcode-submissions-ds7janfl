class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        Input:
            List of List, that contain a start and an endpoint
            Output: List of list, that contain the merged interval points
                [[1,3],[1,5], [6,7]] -> [[1,5],[6,7]]
                The first two entries have an overlap
            Questions:
                What is defined as an overlap?
                    if the start of a new interval is less than or equal to the end of the previous
                Do I have to keep merging until there is no overlap?
                What do I do when I encounter a non-overlap? Do I create a new list?
            Assumptions:
                The list is not sorted
            Approach Ideas:
                sort the inputs
                Insert the first input into a result list
                for each iterval after there compared if the start is less than or equal to the previous end, if it is merge the overlap
                if it isn't add it to the list and continue


        """ 
        if not intervals:
            return []
        
        if len(intervals) == 1:
            return intervals


        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:
            if  interval[0] <= res[-1][-1]:
                res[-1][-1] = max(interval[-1],  res[-1][-1] )
            else:
                res.append(interval)
        return res







