# https://leetcode.com/problems/jump-game/
# medium

class firstAttempt:

    # 11 / 26 / 2025 - 4:17 pm

    # not working, really close. 170 / 175 test cases passed.

    # boutta go to work and come back to finish this.

    def canJump(self, nums: List[int]) -> bool:
        
        idx = 0

        while idx < len(nums):

            jump = idx + nums[idx]

            if jump >= (len(nums) - 1):
                return True

            if nums[idx] > 0:
                if nums[jump] == 0:
                    nums[idx] -= 1
                    continue
                else:
                    idx += nums[idx]
            else:
                break

        return False

class correct:

    # 11 / 27 / 2025 - 2:51 am

    # alright dude it pisses me off looking at this, considering i came back from
    # work, its currently 2:51 am. the answer is always so simple but i tend to overlook
    # it.

    def canJump(self, nums: List[int]) -> bool:

        maxReach = 0

        for i in range(0, len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        
        return True