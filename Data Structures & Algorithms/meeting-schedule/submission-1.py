"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            startA, endA = intervals[i].start, intervals[i].end
            for j in range(i+1, len(intervals)):
                startB, endB = intervals[j].start, intervals[j].end
                if startA<endB and startB<endA:
                    return False
        
        return True
                