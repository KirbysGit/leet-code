# https://leetcode.com/problems/koko-eating-bananas/
# medium

class firstAttempt:

    # 10 / 26 / 2025 - 2:48 pm

    # Runtime -> 140 ms - 92.28%
    # Memory -> 19.04 MB - 62.73%

    # i had to use chatgpt for a hint because i literally just stared at the problem
    # for like 20 minutes, trying to find a way to solve it. but like i couldn't 
    # understand how to do it with binary search because i keep thinking about it
    # as it has to be applied to the array, instead of what we do in this problem
    # which is apply it to the value of amount of banans per hour.

    # but after understanding that with mr.gpt, it was a simple binary search,
    # where we set up the left and right, then calculate the mid, and as long
    # as left is not equal to right, we calculate the mid, then calculate the 
    # total time needed to get through all the bananas, and if the time is
    # less than h, we update our right value to mid, otherwise if its greater
    # than h, we update our left value to mid + 1. 

    # once the loop converges, we return the right value, (can return either).

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        while left <= right:

            if left == right:
                break

            mid = (left + right) // 2
            time = 0

            for pile in piles:
                time = time + ceil(pile / mid)

            if time > h:
                left = mid + 1
            elif time <= h:
                right = mid


        return right