# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# medium

class firstAttempt:

    # 10 / 16 / 2025 - 3:30 pm
    
    # Runtime -> 98 ms - 37.55%
    # Memory - 20.04 MB - 29.88%

    # one second coming back in a second.

    # alright im back.

    # okay!!! this was kind of a foreign concept for me so i understood how to 
    # approach the problem, but implementation was a struggle, really just understanding how
    # to set up the bfs and the proper up, down, left, right sort of thing.

    # but with the help of mrGPT i got it! but i still need to study more.

    # first off, initialize empty set for visited.

    # call our bfs, main part of the problem.

    # inside the bfs, we add our current position (the entrance) to the visited set.

    # then we increment through our queue, popping off the left side,
    # checking if its an exit, if so we return the steps.
    # if not, we increment our way through the up, down, left, right directions,
    # checking if its a valid move, like within the bounds of the maze, and also
    # not a wall, then if thats valid, we check if we've already visited it,
    # if not, then we add it to visited, then add it to the queue.
    
    # we reference an is_exit check for the sake of simplifying the code,
    # this function just checks if the current position is not the entrance
    # and is on the edge of the maze. if so return true.

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # initialize empty graph    
        visited = set()
        steps = self.bfs(entrance, visited, maze, len(maze), len(maze[0]), entrance)

        return steps

    def bfs(self, start, visited, maze, rows, cols, entrance):
        # initialize our tracking state for points (like x, y)
        visited.add(tuple(entrance))

        # initialize a queue with our entrance as our only pt
        queue = deque([tuple(entrance)])

        # start steps at zero
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if self.is_exit(r, c, rows, cols, entrance):
                    return steps

                for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))

            steps += 1

        return -1

    def is_exit(self, r, c, rows, cols, entrance):
        return (r, c) != tuple(entrance) and (r in (0, rows-1) or c in (0, cols-1))

class anotherSolution:

    # Runtime -> 48 ms - 93.65%
    # Memory -> 19.22 MB - 66.21%

    # found this one set up on the leetcode solutions. a lot simpler.

    # similar sort of approach. im gonna explain it in the code though so look down there dude!

    # alright so a big thing for me is im caught up on the recursing back through
    # options in these sort of graphs. but for this problem we don't need to
    # i was confused why this solution just set all the values to a wall after they 
    # were visited, but then i realized its because they're not actually needed after
    # they've been visited, like as soon as we visited it we get all the possible movements
    # then we don't need to go back and visit it again.

    # people are so smart man! imma be like that.

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        # get dimensions of maze. m = rows, n = cols.
        m,n=len(maze),len(maze[0])
        
        # get entrance coords.
        sr,sc=entrance

        # initialize array for directions (up, down, left, right).
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        # initialize our queue.
        q=deque()

        # add entrance to queue with distance 0.
        q.append((sr,sc,0))

        # mark entrance as visited by changing it to '+'.
        maze[sr][sc]='+'

        while q:
            # pop off left side of queue, getting coords and distance.
            r,c,dist=q.popleft()

            # for each direction.
            for dr,dc in dirs:

                # sum for new coords.
                nr,nc=r+dr,c+dc

                # if new coords are out of bounds, continue.
                if not (0<=nr<m and 0<=nc<n):
                    continue

                # if new coords are a wall, continue.
                if maze[nr][nc]=="+":
                    continue

                # if new coords are an exit, return the distance + 1.
                if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                    return dist+1

                # update current coords to a wall.
                maze[nr][nc]='+'

                # add new coords to queue with distance + 1.
                q.append((nr,nc,dist+1))

        # if no exit found, return -1.
        return -1