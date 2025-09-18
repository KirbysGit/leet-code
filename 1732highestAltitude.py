# https://leetcode.com/problems/find-the-highest-altitude/
# easy

class firstAttempt:
    # 09 / 18 / 2025 - 3:34 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.67 MB - 81.98%

    # alright all by mysel again, no GPT, but also this one is super easy,
    # just iterate through gain, adding height to curHeight then checking if 
    # the current height is greater than the max height, if so update the max

    # pretty simple, might be a better way to do it with memory but i gotta think

    def largestAltitude(self, gain: List[int]) -> int:
        
        curHeight, maxHeight = 0, 0

        for height in gain:
            curHeight = curHeight + height
            if (curHeight > maxHeight):
                maxHeight = curHeight
            
        return maxHeight