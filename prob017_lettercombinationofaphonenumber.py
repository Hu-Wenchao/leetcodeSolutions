"""
Given a digit string, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the
telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ph = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        res = ['']
        for d in digits:
            tmp = []
            for c in ph[d]:
                tmp += [term + c for term in res]
            res = tmp
        return res
