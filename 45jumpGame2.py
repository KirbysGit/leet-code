# https://leetcode.com/problems/jump-game-ii/
# medium

class firstAttempt:

    # 11 / 28 / 2025 - 12:25 am

    # had to use chatgpt, i couldn't wrap my head around it. ill come back to this when i 
    # get back to o-town tmrw, but i get what its doing in hindsight, but just like figuring it
    # out as i work through it makes no sense to me.

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        end = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest
        
        return jumps