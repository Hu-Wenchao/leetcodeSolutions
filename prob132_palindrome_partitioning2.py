"""
Given a string s, partition s such that every 
substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome 
partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] 
could be produced using 1 cut.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # cut numbers in worst case (no palindrome)
        cut = [x for x in range(-1,len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge
            # radius if a palindrome exists
            # odd palindrome
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even palindrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]
