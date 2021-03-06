"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, 
return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Idea:
        # 1. last bit of (odd number & even number) is 0.
        # 2. when m != n, There is at least an odd number
        #    and an even number, so the last bit position result is 0.
        # 3. Move m and n right a position.
        # Keep doing step 1,2,3 until m equal to n,
        # use a factor to record the iteration time.
        
        if m == 0:
            return 0
        factor = 1
        while m != n:
            m >>= 1
            n >>= 1
            factor <<= 1
        return m * factor
