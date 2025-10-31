# https://leetcode.com/problems/min-cost-climbing-stairs/
# easy

class firstAttempt:

    # 10 / 30 / 2025 - 2:22 pm 

    # Runtime -> 2 ms - 79.59%
    # Memory -> 17.83 MB - 63.29%

    # pretty simple overall, I might've overcomplicated it with my set up
    # but the overall approach is the same.

    # the idea is we work backwards, starting at the last two steps, and check
    # the cost of taking the 1st step or the 2nd step, and we take the minimum of
    # the two and add it to the current steps cost, and do this working backwards
    # until we get back to the first step.

    # this basically allows us to see how much it would cost to get from the cur step
    # to the last step taking the smallest cost. like we can look at like 6th step
    # and see what the minimum cost would be to get to the last step is from there.

    # the set up is initialize an arary, set the last two values to cost[n - 1] and 0.
    # then working backwards, update the current step to the minimum of the two options
    # and add it to the the current cost. then when we get back to the first step
    # return the least of the 0th and 1st index as thats the cheapest route.

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0] * (n + 1)
        dp[n] = 0
        dp[n - 1] = cost[n - 1]
        total = 0

        i = n - 2
        while i >= 0:
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
            i-=1

        if dp[0] > dp[1]:
            return dp[1]
        
        return dp[0]

class anotherSolution:

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.83 MB - 63.29%

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] is the min cost to reach i 
        prev_1 = 0
        prev_2 = 0 
        for i in range(2, n + 1):
            cur = min(prev_1 + cost[i - 1], prev_2 + cost[i - 2])
            prev_2 = prev_1 
            prev_1 = cur 
        return cur 

    # they set it up that instead of storing the entire dp array.
    # the only keep the last two states you need to compute the next one.

    # basically prev_2 is the cost to reach i - 2, and prev_1 is the cost to reach i - 1
    # so per step, i, they are computing cur then sliding the window.

    # its just a sliding window sort of approach. so to compute our dp[i], you only
    # need the previous two values, so every iteration you 