# https://leetcode.com/problems/rotate-array/
# medium

class firstAttempt:

    # 11 / 23 / 2025 - 2:32 pm

    # Runtime -> 3 ms - 74.71%
    # Memory -> 25.87 MB - 9.08%

    # no gpt! i had the idea of like iterating through but i didn't really preserve it
    # well, but imma try to do that in a second. but basically all i did was like take
    # the last k elements, and add them to the front of the array, then take the rest and 
    # basically at them to the end of the array.

    # just a lil magic with slices.

    # also needed to handle the case where k is great than n because the slice wouldn't
    # work so we just do k % n to get the the actual number of elements to rotate.

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n < k:
            k = k % n

        tmp = nums[(n - k):n]
        ex = nums[0:(n - k)]
        
        nums[0:k] = tmp
        nums[k:n] = ex