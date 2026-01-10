# https://leetcode.com/problems/valid-sudoku/
# medium

class firstAttempt:

    # 1 / 9 / 2026 - 7:55 pm

    # okay this was my first attempt that didn't work. i jsut wanted to add it.
    # basically i was like, let me loop through all the rows, then all of the columns,
    # and it should work!

    # WRONG!!!! i forgot about the 3x3. i referenced chatgpt after that, and i kind of
    # got carried away but i also just wanted to learn how to set it up, i didn't 
    # understand how to target the 3x3 without like 3 sets of loops, so i needed some
    # assistance.

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()
        
        for row in board:
            for char in row:
                if char == ".":
                    continue
                else:
                    if char in seen:
                        return False
                    else:
                        seen.add(char)
            
            seen = set()

        seen = set()

        for row in range(0, 9):
            col = 0
            print(char)
            while col < 9:
                char = board[col][row]
                if char != ".":
                    print(seen)
                    if char in seen:
                        return False
                    else:
                        seen.add(char)
                col += 1

            seen = set()
        return True
            
class correctAttempt:

    # 1 / 9 / 2026 - 7:57 pm

    # Runtime -> 3ms - 81.53%
    # Memory -> 19.33 MB - 5.74%

    # i referenced mr.gpt for this one, but i understand what its doing, the 3x3 indexing is still
    # a little weird but i understand it enough to do some more matrix problems. but basically
    # lets use maps to store each value per like row, col, box, based on a key, then we can just go
    # through it once and check if there is any duplicates as we move through.

    seenRow = [set() for _ in range(9)]
    seenCol = [set() for _ in range(9)]
    seen3x3 = [set() for _ in range(9)]

    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != ".":
                box = (row // 3) * 3 + (col // 3)
                if num in seenRow[row] or num in seenCol[col] or num in seen3x3[box]:
                    return False
                else:
                    seenRow[row].add(num)
                    seenCol[col].add(num)
                    seen3x3[box].add(num)
    
    return True