# https://leetcode.com/problems/evaluate-division/
# medium

class firstAttempt:

    # 10 / 16 / 2025 - 2:16 am

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.82 MB - 72.73%

    # HOLY FUCK!!!!!
    # this might be my longest one yet. had to use chatgpt a bunch, i never let it
    # give me answers, just hints however. 

    # but my idea for this problem changed like 10 times over the course of trying
    # to solve it. but it started out making sure i set the graph up right, with
    # the double edged values.

    # i had the idea for how to solve the problem down pretty well, but incorporating
    # recursion and storing of the proper values and the visited array was confusing
    # as fuck for me.

    # eventually however i was like okay we need to go through each query, and per
    # query assuming both values exist and are not just the same, we will need
    # to dfs through our graph and find the second value somewhere, and while doing
    # that we need to properly multiply the values along the way, this was
    # very hard conceptually to understand, now that i have the answer its very
    # simple in code, but i still get a headache thinking about the recursive process
    # on bigger test cases.

    # but answers, i knew it was dfs, and we need to visit each point, then check
    # if we've already visited it, if not, then we can check if its equal to denom, then if
    # not we gotta recurse again. 

    # my main issue towards the end there was how i was passing the val value i had stored,
    # as well as the proper handling of going past the first iteration of the for loop
    # without just returning that answer, like i didn't realize that it was just 
    # returning -1 after the first check in the dfs.

    # the thing we're doing to solve what i was struggling with is literally just the 
    # check that if the recursed result is not -1, then return that, so if it is -1 we
    # just keep going through the loop. 

    # also gonna throw this on there for the sake of proof : 

    # Time taken: 3 d 19 hrs 10 m 35 s

    class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        # setting up the graph with the adjacency list.
        n = len(equations)
        graph = {}
        for (num, denom), val in zip(equations, values):
            graph.setdefault(num, []).append((denom, val))
            graph.setdefault(denom, []).append((num, 1 / val))

        # initialize empty list for storing answers
        answers = []

        # iterate per pair in queries
        for a, b in queries:
            
            # original check, if either not in graph, add -1 and continue
            if a not in graph or b not in graph:
                answers.append(-1.0)
                continue

            # second check, if the values == each other then value = 1, then continue
            if a == b:
                answers.append(1)
                continue

            # initialize a fresh set.
            visited = set()

            # dfs.
            answers.append(self.dfs(a, b, graph, visited, 1))


        return answers

    def dfs(self, num, denom, graph, visited, val):
        # add cur node to visited.
        visited.add(num)

        # per edge from node.
        for a, b in graph[num]:
            # if node not visited.
            if a not in visited:
                # if new node is the node we're looking for, return val * cur val.
                if a == denom:
                    return val * b

                # else, recurse again.
                result = self.dfs(a, denom, graph, visited, val * b)

                # and after recursing if result is not -1, return that.
                if result != -1.0:
                    return result

        # else, return -1.0
        return -1.0