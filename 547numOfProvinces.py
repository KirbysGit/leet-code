# https://leetcode.com/problems/number-of-provinces/
# medium

class firstAttempt:

    # 10 / 12 / 2025 - 3:25 pm

    # Runtime -> 7 ms - 55.71%
    # Memory -> 18.70 MB - 99.46%

    # alright i had to use mrgpt.

    # i was really struggling to conceptually understand how to update the visited
    # array without like doubling over or like handling combined provinces without
    # just noting both cities in the province.

    # but basically i get what its doign now, im just still new to graphs so 
    # its a learning curve. but anyways, basic, iteration through the cities,
    # which is just an adjacency matrix, then we check if city hasn't been
    # visited, if so, then dfs through the city arr, updating the number of 
    # provinces by one.

    # in that dfs we will mark each city that we can visit as we go through
    # then so when we iterate to the next city, if we already visited it, we
    # can know its been connected. 

    # the way we're checking if we can go to the city is with that check in the 
    # dfs with the if isconnected[i][j] == 1. then we continue the dfs down.

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False] * n
        i = 0
        provinces = 0

        while i < n:
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                provinces+=1

            i+=1

        return provinces

        
    def dfs(self, i, isConnected, visited):
        if visited[i]:
            return

        visited[i] = True

        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(j, isConnected, visited)

    # makes sense but i don't know if i would've understand the visited array
    # set up without mrGPT.

    