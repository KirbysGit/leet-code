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