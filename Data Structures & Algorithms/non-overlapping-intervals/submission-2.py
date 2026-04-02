class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #input: a list of lists that contain a start and end for intervals
        #output: a number that represents thenumber of removals
        # overlapping occurs when the start of the input, and less than the end of the previous input
        # I must keep track of what the latest input is
        # 
        

        counter = 0
        intervals.sort(key=lambda x:x[0])
        recent_end = intervals[0][-1]


        for start, end in intervals[1:]:
            if start < recent_end:
                counter +=1
                # [[1,2], [1,4],[2,4],]
                recent_end = min(recent_end, end)
            else:
                recent_end = end
        return counter

        
        
     

   


            
                
       



