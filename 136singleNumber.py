# https://leetcode.com/problems/single-number/
# easy

class firstAttempt:

    # 11 / 07 / 2025 - 1:44 pm

    # Runtime -> 7 ms - 32.17%
    # Memory -> 19.38 MB - 99.17%

    # alright my thought process was how can we organize the numbers so that we
    # can find the single number, so im like if we have no order its pretty hard
    # other than keeping like an array of what we've seen so far. but that wasn't
    # the constant extra space that we're allowed to use. 
    
    # so i thought about sorting it, and when we have it like that then we know that
    # if the numbers exist in pairs, then there will be as ingle number that is 
    # not in the pair, so if we increment by 2, then we can find the single number at 
    # some point in our process.

    # thats what led me to the solution below, basically, increment through the pairs
    # until we find a pair that doesn't match, then we return the number at the current index.

    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
        
        return nums[i]

class usingXOR:

    # Runtime -> 0 ms - 100.00% 
    # Memory -> 19.57 MB - 76.84%

    # this was under the solutions section, i didn't think about using this, i mean i 
    # honestly forgot it existed. but its such a smart solution. it uses the XOR operator
    # this allows for us to basically cancel out the numbers that are in pairs.

    # like for the example, [4, 1, 2, 1, 2], it will go like :

    # 4 (100) ^ 1 (001) = 5 (101)
    # 5 (101) ^ 2 (010) = 7 (111)
    # 7 (111) ^ 1 (001) = 6 (110)
    # 6 (110) ^ 2 (010) = 4 (100)

    # holy shit its so smart!!

    # but yea really simple.

    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        for i in range(1,n):
            ans^=nums[i]
        return ans