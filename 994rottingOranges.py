# https://leetcode.com/problems/rotting-oranges/
# medium

class firstAttempt:

    # 10 / 19 / 2025 - 8:28 pm

    # Runtime -> 3 ms - 81.56%
    # Memory -> 17.64 MB - 93.32%

    # had to use chatgpt :( moreso just for like syntax and overall small details
    # but i'd like to say i knew the big stuff.

    # pretty similar to the other one we did. so basically like setting up
    # the grid, except with this one we're not given the locations of the oranges,
    # so we had to find them ourself, that ended up being an issue for me,
    # idk why i couldn't figure a set of nested for loops out to get the right
    # q set up. but anyways eventually did (had to use range(), god i feel dumb).

    # looking at the problem tho, the set up to the last maze problem is basically
    # identical except again, get locations of rotten oranges, so i iterated through
    # the maze looking for the 2s. 

    # then bfs through the q, checking per level and incrementing the minutes.
    # during the check we check up, down, left and right, checking if new
    # coords are within the bounds, if they were not empty (= 0), and if they
    # weren't already rotten (= 2), if so we update the grid value to 2 (because
    # we can assume the was 1, meaning it is now rotten), then appened the new
    # rotten orange to the q.

    # then at the end to handle to overall check if there was an unreachable orange,
    # we can then check if there is any 1 left in the entire grid, if so return -1.
    # then check if time is = 0, return 0, because we don't want to decrement
    # below 0 if the time is actually 0. but if time is greater than 0, return time - 1,
    # to get rid of the last ticker increment. set up is here. bfs graph is pretty similar.
    # gonna take some notes on it.

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        q = deque()
        r, c = 0, 0 

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    if grid[nr][nc] == 2:
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            time+=1
        
        if any(1 in row for row in grid):
            return -1

        if time == 0:
            return 0
        
        return time - 1