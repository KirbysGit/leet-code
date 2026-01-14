# https://leetcode.com/problems/rotate-image/
# medium

class firstAttempt:

    # 1 / 13 / 2026 - 9:24 pm

    # im the goat.

    # so i spent like 3 hours on this, doing it on the whiteboard in the kitchen,
    # trying to understand the pattern of the movements and how we have to move
    # the elements. but i got it! i literally did like one submission and got it!

    # basically i drew out the movements, wrote down the pattern in terms of i, j, n
    # then kind of mapped it out to the code with like a reverse flip sort of thing
    # with one tmp.

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.50 MB - 9.25%

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        front, back = 0, n - 1
        for i in range(0, n // 2):
            for j in range(front, back):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = trmp
            front += 1
            back -= 1
        
    # im literally so goated.
    # im honestly the most suprised i got the like funnel shape of the indexes right.

class anotherCorrect:

    # this one is just as fast, chatgpt gave it to me, its way faster than my approach.
    # but i do like mine more because its mine.

    # this is like lets flip all the diagonals, then reverse each row.
    
    # i would've never thought of it.

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

        for row in matrix:
            row.reverse()