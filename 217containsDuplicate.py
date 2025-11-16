# https://leetcode.com/problems/contains-duplicate/
# medium

class firstAttempt:
    
    # Runtime -> 3ms - 98.98%
    # Memory -> 31.58 MB - 53.79%

    # super simple, set gets rid of duplicates, if length of set and
    # length of og list are different, then there are duplicates.

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))