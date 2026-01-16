# https://leetcode.com/problems/game-of-life/
# medium

class firstAttempt:

    # 1 / 15 / 2026 - 7:21 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.36 MB - 12.84%

    # first try baby!!! this was all me. i had to consult gpt for some general shit
    # but it wasn't on how to do the problem it was how to set up a 2D matrix with
    # values and how to parse tuples.

    # but after that i got it!

    # honestly i thought this solution was going to be way too slow because its two
    # O(n^2) loops with like an O(n * m * 8) for the first one so im like wtf??
    
    # but its actually an optimal solution which is so W!!!

    # basically my idea was just to like iterate through each space, checking all the 8
    # directions, checking if that space + dir is in bounds, then just adding up the neighbors
    # and add the amount into another 2 matrix that i then itearte back through after going through
    # all the cells the first time, just checking if the value at i, j qualifies for any of the rules.

    def gameOfLife(self, board: List[List[int]]) -> None:

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                cells = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy

                    if x >= n or y >= m or x < 0 or y < 0:
                        continue

                    if board[x][y] == 1:
                        cells += 1

                neighbors[i][j] = cells

        for i in range(n):
            for j in range(m):
                if neighbors[i][j] < 2:
                    board[i][j] = 0
                elif neighbors[i][j] > 3:
                    board[i][j] = 0
                elif neighbors[i][j] == 3:
                    board[i][j] = 1