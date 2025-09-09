# https://leetcode.com/problems/product-of-array-except-self/
# medium

class firstAttempt:

    # i had to use chatgpt because i couldn't get around the division in my head
    # two passes still doesn't click in my brain, it makes sense walking through, 
    # but i feel im missing out on the pattern

    # Runtime -> 16ms - 93.58%
    # Memory -> 23.29 MB - 79.83%

    # idea is to do two passes, with running products

    # first pass is to use left, where we store the prod of everything before i
    # into final[i], then we update left so the idx sees another factor

    # second pass is to use right, where we store the prod of everything after i
    # and then update right so the idx sees another factor

    # then we return the final array

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [0] * len(nums)

        left = 1
        for i in range(len(nums)):
            final[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            final[i] *= right 
            right *= nums[i]

        return final