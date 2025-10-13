# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# medium

class firstAttempt:

    # 10 / 13 / 2025 - 2:21 pm
    
    # Runtime -> 208 ms - 43.44%
    # Memory -> 53.57 MB - 13.87%

    # holy shit. this problem is so confusing to me, i had to use chatgpt and i still really
    # don't understand it. i'm gonna take some notes, but like every aspect of it is just
    # so weird.

    # basically we just want to reverse all the roads that lead to city 0 that don't already point
    # that direction.

    # i was getting caught up on the recursion  or like setting it up with the arrays and it didn't
    # and doesn't really make sense to me.

    # i'll probably come back with an explanation but i'll drop the code then im gonna go study
    # it and take some notes because holy FUCK!! i don't get it.

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        visited = n * [False]
        total = 0
        
        graph = {i: [] for i in range(n)}
        for a, b, in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        total = self.dfs(0, visited, graph)
        
        return total
        
    def dfs(self, cur, visited, graph):
        visited[cur] = True
        total = 0
        for neighbor, needsReverse in graph[cur]:
            if not visited[neighbor]:
                total += needsReverse + self.dfs(neighbor, visited, graph)

        return total