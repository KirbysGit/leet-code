# https://leetcode.com/problems/minimum-size-subarray-sum/
# medium

class firstAttempt:

    # 01 / 02 / 2026 - 7:07 pm

    # Runtime -> 15 ms - 21.83%
    # Memory -> 28.16 MB - 74.30%

    # this shit is / was pissing me off. spent a couple days on it. says i took 7 days, but i think
    # i opened it up and gave it like a minimal attempt then just left it.

    # but anyways, bro i tried like a shrinking array, where like you have both sides and move in, but
    # it can be too slow if we take the sum of the window over and over again as it becomes O(n^2).

    # also i tried sorting it but it has to remain in the order to find the best possible array from
    # the original which is stupid as fuck.

    # but anyways, i had to use chatgpt for hints and im also just so tired from being on a plane and 
    # feeling a bit sick, but i was like i need to just understand how to do this because like i get it
    # but i don't. i knew it was sliding window, but the way it moved was hurting my head, like trying to
    # visualize it and how many possible cases it could be if done wrong (the way i was thinking about it).

    # the correct way to do it is basically, left and right, start and just expand array until the sum
    # is great than the target, then from there we start shrinking the array from the left until the sum is
    # less than the target, then we update the best current window size. 

    # its still a bit confusing but i understand it better. 

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        if max(nums) == target:
            return 1

        count = float('inf')
        left = 0
        right = 0
        cur = 0
        while right < len(nums):
            cur += nums[right]
            if cur >= target:
                while cur >= target:
                    cur -= nums[left]
                    left += 1
                    count = min(count, right - left + 1)
            
            right += 1
        
        return count + 1

class secondAttempt:

    # noticed how slow the sum could be making it off rip, so i just got rid of the initial
    # statements and it sped up a bit.

    # Runtime -> 11 ms - 48.12%

    # im guessing it has to do with our while loop set up not breaking early enough that its still
    # not that high of a percentage but idk.

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        count = float('inf')
        left = 0
        right = 0
        cur = 0

        while right < len(nums):
            cur += nums[right]
            if cur >= target:
                while cur >= target:
                    cur -= nums[left]
                    left += 1
                    count = min(right - left + 1, count)
            
            right += 1
        
        return 0 if count == float('inf') else count + 1
            

class thirdAttempt:

    # alright this was mrGPT. but using a for loop (obvious in hindsight because of how loop was 
    # set up), and getting rid of the if statement with the while loop, it sped up a lot.

    # Runtime -> 7 ms - 92.95%
    # Memory -> 27.78 MB - 98.05%

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        count = float('inf')
        left = 0
        cur = 0

        for right in range(len(nums)):
            cur += nums[right]

            while cur >= target:
                count = min(count, right - left + 1)
                cur -= nums[left]
                left += 1

        return 0 if count == float('inf') else count