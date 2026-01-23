# https://leetcode.com/problems/contains-duplicate-ii/description/
# easy

class firstAttempt:

    # 01 / 23 / 2026 - 2:08 pm

    # Runtime -> 106 ms - 5.22%
    # Memory -> 46.77 MB - 5.09%

    # alright this one was weird as fuck at first and obviously i still
    # don't have a great answer for it from this response below, but i was just
    # thinking like we hash the values out, then we can just check if the 
    # values are within k of each other, if they are at some point, return true.

    # i think the sub-check is really whats making it slow, so i'll try
    # to find another way to do this.

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        idxPairs = defaultdict(list)

        for idx in range(0, len(nums)):
            idxPairs[nums[idx]].append(idx)

        for key, vals in idxPairs.items():
            if len(vals) > 1:
                for idx in range(1, len(vals)):
                    if vals[idx] - vals[idx-1] <= k:
                        return True
        
        return False

class secondAttempt:

    # 01 / 23 / 2026 - 2:21 pm

    # TIME LIMIT EXCEEDED

    # crazy how i got slower, but i used gpt for a hint, and kind of only
    # read the first sentence and it was like "Have I seen this number recently?"
    # within k steps. and i was like okay lets do a sliding window of sorts and check
    # if the len of the window is the same as the len of hte set of the window, if so,
    # then there is no duplicates.

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k >= len(nums):
            if len(set(nums)) != len(nums):
                return True
            else:
                return False

        for idx in range(k, len(nums)):
            slide = nums[idx - k : idx + 1]
            window = len(slide)
            dups = len(set(slide))
            if window != dups:
                return True

        return False

class thirdAttempt:

    # 01 / 23 / 2026 - 2:39 pm

    # Runtime -> 7 ms - 99.66%
    # Memory -> 33.52 MB - 64.46%

    # this was all me!!! im the goat!!!
    # basically i was just trying to prevent some of the break cases that
    # were causing it to be slow. and i used a set to kind of doing 
    # a sort of sliding window.

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) == len(set(nums)):
            return False
        
        stack = set()

        if k == 0:
            return False
        
        for idx in range(0, len(nums)):
            if nums[idx] in stack:
                return True
            else:
                if len(stack) > k - 1:
                    stack.remove(nums[idx - k])
                
                stack.add(nums[idx])
        
        return False