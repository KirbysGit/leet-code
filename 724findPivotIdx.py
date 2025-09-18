# https://leetcode.com/problems/find-pivot-index/
# easy

class firstAttempt:

    # 09 / 18 / 2025 - 3:43 pm

    # Runtime -> 0ms - 100.00%
    # Memory -> 18.76 - 38.72%

    # ^ these values keep changing when i submit but pretty sure its one of the fastest solutions

    # but basically same idea as the last one i did like 10 minutes ago, leftSum and rightSum
    # iterate through the nums, subtracting current value from rightSum, then checking if they
    # are equal, if so return the index, if not add the current value to leftSum and continue
    # if we reach the end, then just return -1

    # got it really fast. I'M THE GOAT!!!!!!

    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = 0
        rightSum = sum(nums)

        for idx in range(len(nums)):
            rightSum = rightSum - nums[idx]
            if (rightSum == leftSum):
                return idx
            
            leftSum = leftSum + nums[idx]

        return -1