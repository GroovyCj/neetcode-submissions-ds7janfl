"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Input: a list of int, int pairs, representing start and end times
        Output: Boolean: true false
            Return true if there are no overlaps
            Return False if there are
        Questions:
            What determines an overlap?
                if the start time for one meeting is before the endtime of a earlier meeting
            Are the meetings in sequatial order?
                if not can I sort them?
   
        Anti-Assumptions:
            I cannot assume that all meetings are ordered as it does not mention it
        Assumptions:
            I must sort the interval pairs to put them in ascending order
        High-level-Approach:
            Sort the List[tuples] in ascending order based on the start dates
            check to see if the start date for the coming interval is before the end date of the previous date
                From there I can early ecist
        
        """
        if len(intervals) <= 1:
            return True


        intervals.sort(key=lambda x: x.start)


        curr_end = intervals[0].end

        for i in intervals[1:]:
            if i.start < curr_end:
                return False 
            else:
                curr_end = i.end
        return True

    
