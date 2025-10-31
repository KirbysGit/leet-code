# https://leetcode.com/problems/house-robber/
# medium

class firstAttempt:

    # 10 / 31 / 2025 - 2:45 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.61 MB - 82.41%

    # dynamic programming is brutal. bro i fucking suck at it right now.

    # i also feel off right now and just not in the mood to do this, but i felt i should
    # at least learn how to do the problem so i used mr.gpt. 

    # overall, same set up as the last one, 746. but just handling how we add is different
    # i really just don't understand how its keeping track of the "best" solution, that
    # just hasn't clicked for me yet. 

    # set up is initialize dp array. then iterate through, per index tracking the 
    # highest amount we could have up to that point. (this is what i don't really understand)

    # then just return the last index of the dp array.

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]
            