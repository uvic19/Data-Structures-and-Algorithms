"""
Problem: 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        seen = set()

        for i in range(9):
            for j in range(9):
                cell = board[i][j]

                if cell == '.':
                    continue

                row = ('row', i, cell)
                col = ('col', j, cell)

                box_idx = (i // 3) * 3 + (j // 3)
                box = ('box', box_idx, cell)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True

# --- Time & Space Complexity ---
# TC: O(1)
# SC: O(1)
