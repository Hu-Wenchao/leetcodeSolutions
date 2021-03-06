"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially 
adjacent cell, where "adjacent" cells are those horizontally 
or vertically neighboring. The same letter cell may not 
be used more than once.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find(board, word, i, j):
                    return True
        return False

    def find(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " " # indicate used cell
            # check all adjacent cells
            if i > 0 and self.find(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.find(board, word[1:], i+1, j):
                return True
            if j > 0 and self.find(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.find(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0] # update the cell to its original value
            return False
        else:
            return False
