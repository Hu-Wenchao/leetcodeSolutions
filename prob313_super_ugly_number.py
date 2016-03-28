"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime 
factors are in the given prime list primes of size k. For 
example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the 
sequence of the first 12 super ugly numbers given 
primes = [2, 7, 13, 19] of size 4.
"""

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]
