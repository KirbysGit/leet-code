# https://leetcode.com/problems/set-matrix-zeroes/
# medium

class firstAttempt:

    # 1 / 14 / 2026 - 12:09 pm

    # Runtime -> 23 ms - 5.13%
    # Memory -> 20.38 - 6.19%

    # alright so i looked at this problem yesterday night and thought of this randomly
    # right after i woke up. because i was like its another one of those stupid "in space"
    # ones. and i didn't know how to avoid like turning the entire matrix into zeroes
    # with like setting a column to zero and then seeing that zero and being like oh now we
    # need to turn the entire row to zeroes.

    # and then i just would append the row and column if zero to a list.
    # then do a second iteration through checking if row or column in the list,
    # then set the current value to zero.

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        columns = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0

class secondAttempt:

    # 1 / 14 / 2026 - 12:14 pm

    # whelp i was just typing out the solution to the last one and
    # the cursor tab mentioned a set, and i was like oh shit that would
    # be way faster than an array checking membership in.

    # so i adjusted it and submitted and got this :

    # Runtime -> 0 ms - 100.00%
    # Memory -> 20.04 MB - 9.38%

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        columns = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0