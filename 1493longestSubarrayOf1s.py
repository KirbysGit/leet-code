# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# medium

class firstAttempt:

    # this really was my first attempt!

    # no chatGPT too!

    # Runtime -> 58 ms - 64.06%
    # Memory -> 21.22 MB - 98.07%

    # idea here is basically another sliding window, but we have to keep track if we already
    # deleted one of the zeros, because if so we got to update our idx. so what were doing here
    # is initial some values, then while iterating through array, if we see a zero, 
    # if we have already deleted one, then while left is less than delIdx we increment left
    # up, thne we increment it up one more just to put it past the idx, then we update
    # delIdx to rights current value for the new zero we deleted, then if we haven't deleted
    # one yet, we update delIdx to right and set alreadyDeleted to True. then we update the best
    # by comparing current window size with the best one.

    def longestSubarray(self, nums: List[int]) -> int:
        
        alreadyDeleted = False
        delIdx = 0
        best = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                if alreadyDeleted == True:
                    while (left < delIdx):
                        left+=1
                    left+=1
                    delIdx = right
                else:
                    delIdx = right
                    alreadyDeleted = True
            
            best = max(right - left, best)

        return best