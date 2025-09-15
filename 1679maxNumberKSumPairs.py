# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# medium

class firstAttempt:

    # 09 / 13 / 2025 - 3:53 pm

    # Runtime -> 502 ms - 65.08%
    # Memory -> 30.06 MB - 50.93%

    # alright had to use chatGPt for this one, it was a struggle in fact, 
    # i feel i had the right idea but i just couldn't get around the logic, was
    # trying to handle like a goal value and work from there, but i didn't realize
    # that del was O(n), so doing that was definitely not the way to go

    # so after using chatGPT for a sec, i ended up being able to adjust my code to what
    # you see below, a big thing i wasn't thinking about was sorting, that was huge

    # we start with two pointers, one at the start, then one at the end, then we kind of
    # just check if sum of pointers is equal to k, if it is we increment count and move
    # pointers inwards, if it's greater than k, we decrement the right pointer, if its 
    # less than k we increment the left pointer, then we return the count as soon as 
    # the left pointer is greater than the right pointer

    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        i = 0
        j = len(nums) - 1
        count = 0

        while (i < j):
            if (k - nums[i] < nums[j]):
                j-=1
            elif (k - nums[i] > nums[j]):
                i+=1
            else:
                count+=1
                i+=1
                j-=1

        return count