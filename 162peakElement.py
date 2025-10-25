# https://leetcode.com/problems/find-peak-element/
# medium

class firstAttempt:

    # 10 / 25 / 2025 - 6:10 pm 

    # Runtime - 0 ms - 100.00%
    # Memory - 17.84 MB - 61.29%

    # this one was weird to wrap my head around, i always viewed binary search
    # as it had to be ordered, but this problem doesn't really need that.

    # instead the idea is to binary search but keep track of a property with the
    # mid value, that property is the "slope" in a sense. per middle value we
    # want to check if the value to its right, is greater than the current value
    # (the mid value), if so, then we have an increasing slope, so the peak must
    # be to the right, so we can update our left to be mid + 1. same sort of thing
    # for if its not greater than the right value, then we have a decreasing slope,
    # or we might already be at the peak, so we update the right value to mid.

    # i needed a hint from chatgpt, but it makes sense now, i don't know if it would
    # work if there was just one peak value, but i think it works for our local maximum
    # set up. 

    def binarySearch(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        return self.binarySearch(nums)