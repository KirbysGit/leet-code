# https://leetcode.com/problems/trapping-rain-water/
# hard

class firstAttempt:

    # 12 / 07 / 2025 - 1:24 pm

    # bro i've been working on this for like 2 days, and im still so stuck. 
    
    # basically where im at is like i have the general approach of like finding the volumne
    # left over by the rain. but my issue is handling when i actually check. right now
    # im carrying two pointers where i only update the back if the front is > than the back.

    # so like i can find the valleys and do the math to find the water left over after displacement.

    # i just asked chatgpt for a hint but i don't know if its helping me that much.

    # i tried implementing a stack for the values and it worked for the two initial test cases but
    # now my code isn't hadnling the other ones as well. currently at 186 / 324 passed.

    # 12 / 08 / 2025 - 2:39 pm

    # caved in. had to use chatgpt. gave me some sort of hint, i was like wait i can do it with
    # two pointers at edges instead. and so i tried that for a bit, but i just didn't understand the
    # volumne calculation. 
    
    # worked through it with mrgpt for a sec then landed upon the local max sort of thing i was thinking
    # about when i first started it. honestly i don't fully understand it, like i get the idea
    # and how it is working, but like somethings just not clicking because the answer was basically given
    # to me in psuedo code.

    # anyways the solution basically does two pointers, one on left and one on right, it slowly moves inwards
    # trying to find a local max per side. if the left side is taller than the right side it moves the right pointer 
    # in because the rain water is limited by the shorter side. 

    # so as we move in, if we find a new max height per side (leftMax or rightMax), we update that, if
    # the current value is less than the relative max height like the current left value is less than the
    # leftMax, then we calculate the water trapped by the different between the leftMax and the current left height.

    # same for the right side, the checks basically are, which side is higher, then based on that, check if 
    # the current value is less than the relative max height, if so, update, else calculate water trapped. 

    def trap(self, height: List[int]) -> int:

        n = len(height)
        left = 0
        right = n - 1
        leftMax, rightMax = 0, 0

        while left < right:
            
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    area += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    area += rightMax - height[right]
                right -= 1

        return area