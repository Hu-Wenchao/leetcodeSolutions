"""
Given a set of non-overlapping intervals, insert a 
new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted 
according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] 
in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and 
merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps 
with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        if len(intervals) == 0:
            res.append(newInterval)
            return res
        interval = newInterval
        for i in range(len(intervals)):
            interval2 = intervals[i]
            if interval2.end < interval.start:
                res.append(interval2)
            elif interval2.start < interval.start and \
                 interval2.end >= interval.start and \
                 interval2.end <= interval.end:
                interval.start = interval2.start
            elif interval2.start < interval.start and \
                 interval2.end > interval.end:
                interval = interval2
            elif interval2.start >= interval.start and \
                 interval2.end <= interval.end:
                continue
            elif interval2.start >= interval.start and \
                 interval2.start <= interval.end and \
                 interval2.end > interval.end:
                interval.end = interval2.end
            elif interval2.start > interval.end:
                res.append(interval2)
        res.append(interval)
        res = sorted(res, key = lambda interval:interval.start)
        return res

    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda interval:interval.start)
        interval = intervals[0]
        res = []
        for interval2 in intervals[1:]:
            if interval.end < interval2.start:
                res.append(interval)
                interval = interval2
            else:
                interval.end = max(interval.end, interval2.end)
        res.append(interval)
        return res

