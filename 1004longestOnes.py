# https://leetcode.com/problems/max-consecutive-ones-iii/
# medium

class firstAttempt:

    # i felt i had the right idea but man i just couldn't get around the logic,
    # i had a pretty close first attempt which ill show below : 

    # the issue here was the idx = front
    # which i understood but like i didn't understand how i could increment the left
    # idx without doing another while loop, but its kind of what we ended up doing anyways

    def longestOnes(self, nums: List[int], k: int) -> int:
        
        availableZeros = k
        maxWindow = 0
        curWindow = 0
        front = 0
        idx = 0

        while (idx < len(nums)):
            if nums[idx] == 1:
                curWindow+=1
                idx+=1
            else:
                if availableZeros > 0:
                    curWindow+=1
                    idx+=1
                    availableZeros-=1
                else:
                    front+=1
                    idx = front
                    availableZeros = k

                    if curWindow > maxWindow:
                        maxWindow = curWindow

                    curWindow = 0
    
        
        if curWindow > maxWindow:
            maxWindow = curWindow

        return maxWindow


class firstCorrectAttempt:

    # had to use chatGPT, FUCK!!!!!

    # Runtime -> 79 ms - 63.43%
    # Memory -> 20.45 MB - 16.47%

    # idea here is basic declarations, then from there
    # iterate through nums arr, if the end of the window is zero, increment zerosUsed
    # then to handle the case where zerosUsed is greater than k, we decrement zerosUsed
    # in a while loop, and increment the left accordingly, then we update the best
    # by comparing with the previous best and the current window size which we get
    # from subtracting left from right and adding 1

    # pretty simple but it still not clicking, gotta do it more

    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        zerosUsed = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zerosUsed +=1

            while zerosUsed > k:
                if nums[left] == 0:
                    zerosUsed-=1
                
                left+=1
            
            best = max(best, right - left + 1)

        return best