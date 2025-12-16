# https://leetcode.com/problems/zigzag-conversion/
# medium

class firstAttempt:

    # 12 / 15 / 2025 - 5:03 pm

    # still no solution. trying to think through if theres a formula we can use.
    # like n - 1 * 2 for the first and last row. or like just a while loop to try to
    # walk through to append the correct indexes to the rows.

    def convert(self, s: str, numRows: int) -> str:

        n = len(s)
        
        if numRows == 1 or n == numRows:
            return s

        idxRows = [numRows][]

        row = 0
        idx = 0
        steps = 0

        while steps < n:
            idxRows[row].append(idx)
            idx+=1
            steps+=1

class gptHint:

    # 12 / 16 / 2025 - 2:46 pm

    # got it, i like understood the idea, but like walking through it made no sense.
    # i was tryin to like double walk through the indexes with a for loop thne handling the
    # rows separately but it doesn't work. 

    # mr.gpt hinted at just using the chars then doing the zig zag with a direction variable.
    # from there it was just like how we walk up and down. so basically like we're increasing rows 
    # as long as direction is -1, and then once we hit the bottom row, then we change the direction
    # to 1 and work backwards as we go through the chars adding them to a 2D array.

    # simple in hindsight, no idea though after like 3 hours of staring at it.

    # Runtime -> 3 ms - 98.95%
    # Memory -> 17.92 MB - 49.32%

    def convert(self, s: str, numRows: int) -> str:

        n = len(s)

        if n == 1 or numRows == 1:
            return s

        idxRows = [""] * numRows

        row = 0
        direction = -1

        for char in list(s):
            idxRows[row] += char

            if direction == -1:
                rows +=1 
            else:
                row -= 1

            if row == numRows - 1:
                direction = 1
            elif row == 0:
                direction = -1

        return "".join(idxRows)