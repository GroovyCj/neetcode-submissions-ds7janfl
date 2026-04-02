class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])
        counter = 0
        prev_end = intervals[0][-1]
        print(intervals)
        
        
     

       
        for start, end in intervals[1:]:
            if start < prev_end:
                counter += 1
                if prev_end > end:
                    prev_end = end
            else:
                prev_end = end
                  
        return counter

    


            
                
       



