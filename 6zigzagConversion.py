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