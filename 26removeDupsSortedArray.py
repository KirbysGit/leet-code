# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# easy

class firstAttempt:

    # 11 / 20 / 2025 - 2:10 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.29 MB - 8.12%

    # this one was basically like the other one i did except just
    # used the sort method on the array. looking through the solutions 
    # it doesn't really look like anyone else used it like that, but
    # it works and its fast so!

    # literally just convert to set to get rid of duplicates, then back to list, copy that
    # to the nums, then sort nums and return the length of the new array.

    def removeDuplicates(self, nums: List[int]) -> int:
        
        nums[:] = list(set(nums))
        nums.sort()

        return len(nums)


class otherWay:

    # a bit more complicated but like a two-pointer approach, just having one pointer at the 
    # first new value and one at the end. iterate through the array, if the value at the 
    # first pointer is not equal to the value at the second pointer, we swap, then increment
    # the first pointer.

    def removeDuplicates(self, nums: List[int]) -> int:
        
        true_i = 1
        new_i = 1
        while true_i < len(nums):
            if nums[true_i] != nums[new_i - 1]:
                nums[true_i], nums[new_i] = nums[new_i], nums[true_i]
                new_i += 1
            true_i += 1
        return new_i