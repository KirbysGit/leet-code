# https://leetcode.com/problems/increasing-triplet-subsequence/
# medium

class firstAttempt:

    # i had to use chatGPT again, couldn't get around doing it in O(n)
    # my brain kept reverting back to incrementing through each possible idx

    # Runtime -> 11ms - 95.66%
    # Memory -> 37.59 MB - 22.85%

    # idea behind this is greedy, we keep track of the smallest and middle values
    # so like if we set a value in second, that means there is a value that is smaller
    # before it, and if we then find a value, that is greater than the middle, that means
    # we have a triplet, becasue second can only exist if there is a value smaller than it

    # my brain is still learning to think outside of brute force, its a struggle

    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        middle = float('inf')

        for x in nums:
            if x <= smallest:
                smallest = x
            elif x <= middle:
                middle = x
            else:
                return True

        return False

