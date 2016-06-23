"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda interval:interval.start)
        interval = intervals[0]
        ret = []
        for interval2 in intervals[1:]:
            if interval.end < interval2.start:
                ret.append(interval)
                interval = interval2
            else:
                interval.end = max(interval.end, interval2.end)
        ret.append(interval)
        return ret