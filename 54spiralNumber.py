# https://leetcode.com/problems/spiral-matrix/
# medium

class firstAttempt:

    # 1 / 10 / 2025 - 1:40 pm

    # no solution yet. working throuhg it. code is really long.
    # i just have one extra point at the end of each that i need to 
    # not add. its just with the messiness of our indexing and conditions.

    # organize it tmrw when im back.

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        x = 0
        y = 0

        top = 1
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        direction = 1

        rad = len(matrix) * len(matrix[0])

        spiral = []

        while x >= left or x <= right and len(spiral) <= rad:
            spiral.append(matrix[y][x])

            if x == right:
                while y < bottom:
                    y += 1
                    spiral.append(matrix[y][x])
                right -= 1
                bottom -= 1
                direction = -1
            if x == left and direction == -1:
                while y > top:
                    y -= 1
                    spiral.append(matrix[y][x])
                left += 1
                top += 1
                direction = 1

            if direction > 0:
                x += 1
            else:
                x -= 1
            
        return spiral

class secondAttempt:

    # 1 / 11 / 2025 - 9:17 pm

    # adjusted one line. @ 9 / 26 solutions. 

    # took a break to eat, watched an episode of fire force, came back, and still struggling with
    #  different approach of the same manner. i just think its the way im organizing it that
    # has a lot of issues.

    # coming back tmrw i got it!

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        x = 0
        y = 0

        top = 1
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        direction = 1

        rad = len(matrix) * len(matrix[0])

        spiral = []

        while len(spiral) < rad:
            spiral.append(matrix[y][x])

            if x == right:
                while y < bottom:
                    y += 1
                    spiral.append(matrix[y][x])
                right -= 1
                bottom -= 1
                direction = -1
            if x == left and direction == -1:
                while y > top:
                    y -= 1
                    spiral.append(matrix[y][x])
                left += 1
                top += 1
                direction = 1

            if direction > 0:
                x += 1
            else:
                x -= 1
            
        return spiral
    

class correct:

    # 1 / 12 / 2025 - 7:39 pm

    # had to use gpt for this one, it was a small hint, i literally was explaining things that i was like,
    # its gotta be too slow to do. and then it goes... Nope! thats how you do it!

    # idk why i though the 4 for loops inside a while loop was not quick enough, but i guess i was just
    # not thinking about it the right way.

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.38 MB - 8.24%

    # basically, same thing with the 4 pointers, except we just use 4 for loops with minimal conditions
    # to move up down left and right through the matrix.

    # look at the code and it makes more sense to how we do it (like how we crawl backwards too).

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # initialize pointers.
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        # initialize list for output.
        spiral = []

        while top <= bottom and left <= right:
            # left to right pass.
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1

            # top to bottom pass.
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # right to left pass.
                for col in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # bottom to top pass.
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1

        return spiral