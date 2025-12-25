# https://leetcode.com/problems/3sum/
# medium

class firstAttempt:

    # 12 / 24 / 2025 - 1:50 am

    # its christmas eve and im going home and idk when i would be able to do this other than
    # before work but i don't want to stress myself out over not getting it done and breaking
    # my github streak, so im adding this from the night before. 

    # first attempt, like i looked through and was like "this should work". update: it does NOT!

    # but i definitely think i can figure it out, just gonna come back to it tmrw.

    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        n = len(nums)
        front = 1
        walk = front + 1
        final = []

        while front < n - 1:
            pair = nums[front - 1] + nums[front]
            while walk < n:
                if pair + nums[walk] == 0:
                    final.append([nums[front], nums[front - 1], nums[walk]])

                walk += 1

            front += 1
            walk = front + 1
        
        return final

class secondAttempt:

    # its christmas!!! i work in like less than an hour so i can't really attempt the code,
    # but i'm thinking like a greedy approach to it so we can sort the array and then iterate
    # through the array using three numbers that add to 0 because order doesn't matter.