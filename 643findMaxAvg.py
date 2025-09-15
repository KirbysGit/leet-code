# https://leetcode.com/problems/maximum-average-subarray-i/
# easy

class firstAttempt:

    # 09 / 14 / 2025 - 3:08 pm

    # Runtime -> 39 ms - 95.37%
    # Memory -> 27.45 MB - 39.96%

    # alright so i felt i had the right idea but again the wrong implementation
    # my true first attempt was trying to use the [i:j] method and then just compare
    # those values per group, and it was a window, but the issue was we were adding
    # 3 more values than needed to be added per iteration

    # the solution here is really the same sort of idea with the window, but instead
    # of creating the whole window again and again, because the window always stays
    # the same size, we can just add the new value and subtract the old value to get
    # the new window sum, and then we just compare that with the max and it actually
    # runs in the time bounds to get an accepted answer sooo WOoHOOO! 

    # but yea pretty simple, variables are a little plain, but basicaly add new value
    # subtract old value, then check. pretty simple, hard for me to see.

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        window_sum = sum(nums[:k])
        best = window_sum

        i = 0
        j = k

        for r in range(k, n):
            l = r - k
            window_sum += nums[r] - nums[l]
            if window_sum > best:
                best = window_sum

        return best / k