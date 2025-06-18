from collections import defaultdict
from typing import List

board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


class Solution2:  # hashset one pass. O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(len(board))] # could be just defaultdict(set) too.
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                if val == '.' : continue

                if val in rows[row] or val in cols[col] or val in boxes[(row//3)*3 + col//3] :
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[(row//3)*3 + col//3].add(val)

        return True
    
class Solution3:  # gigachad bitmask
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                num = int(board[i][j]) - 1
                mask = 1 << num                    # Create bitmask for the number
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if the number is already set in the row, column, or box
                if (rows[i] & mask) or (columns[j] & mask) or (boxes[box_index] & mask):
                    return False
                
                # Mark the number in the row, column, and box
                rows[i] |= mask
                columns[j] |= mask
                boxes[box_index] |= mask

        return True
    

if __name__ == "__main__":

    sol1 = Solution1()
    print(sol1.isValidSudoku(board))

    sol2 = Solution2()
    print(sol2.isValidSudoku(board))

    sol3 = Solution3()
    print(sol3.isValidSudoku(board))