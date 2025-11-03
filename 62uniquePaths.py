# https://leetcode.com/problems/unique-paths/
# medium

class firstAttempt:

    # 11 / 02 / 2025 - 1:13 am

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.66 MB - 88.86%

    # i feel like i've done some version of this problem before, but don't really
    # remember it. basically, given a maze, of m x n, and we want to find the number of
    # unique paths from top left to the bottom right. we can only move down or right. 

    # i mean the problem is in the dynammic programming so i knew, but it makes sense
    # that going from usual 1 D to 2 D would be different, but like all we really changed
    # was the way we set up the dp array. my first set up was very close to being correct.

    # i originally set it up without the two for loops to initialize the first row and
    # column because i was thinking about the number of moves, not the path it would take,
    # but then when that was pointed out, it made much more sense and all i had to do was
    # adjust the loop indexing slightly. then i had it!

    # looking at the solution its super simple, just initialize the dp array to 0s.

    # then set the first row and column to 1s.

    # then, itearte through the rest of the array, and per cell add the value of the cell
    # above it, and to the left of it.

    # finally, return the value of the bottom right cell.

    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]