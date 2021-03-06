"""
Given a pattern and a string str, find if str follows the same pattern.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = pattern
        s = str.split()
        return map(p.find, p) == map(s.index, s)
