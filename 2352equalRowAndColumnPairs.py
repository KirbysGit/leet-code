# https://leetcode.com/problems/equal-row-and-column-pairs/
# medium

class firstAttempt:

    # 09 / 21 / 2025 - 2:50 pm

    # Runtime -> 154 ms - 18.22%
    # Memory -> 21.73 MB - 94.78%

    # i had to use chatgpt but i understood how to do it, just didn't understand how to
    # get the columns into their own values. 

    # idea is jsut get the rows into a list, then the columns into a list, then we can
    # iterate through each row and column and compare if they're the same, if so
    # increment the counter, then return it.

    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        columns = []

        for row in grid:
            rows.append(row)

        n = len(grid)

        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            columns.append(col)

        count = 0

        for row in rows:
            for column in columns:
                if row == column:
                    count+=1

        return count

class tupleStrat:

    # Runtime -> 7ms - 97.54%
    # Memory -> 22.03 MB - 36.24%

    # saw this one in solutions tab. uses counters per tuple.

    # basically we get length of grid.
    # initialize a dict w/ default factory of int.
    # iterate through grid, adding tuples to the table and incrementing the value by 1.
    # iterate through again, adding tuples to temp list, and then adding the value of the table
    # at the tuple to the pairs. 
    # then return the pairs.

    def equalPairs(self, grid: List[List[int]]) -> int:

        n=len(grid)

        table=defaultdict(int)

        for i in range(n):
            table[tuple(grid[i])]+=1

        pairs=0

        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(grid[j][i])
            pairs+=table[tuple(temp)]

        return pairs
