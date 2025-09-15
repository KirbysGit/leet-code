# https://leetcode.com/problems/container-with-most-water/
# medium

class firstAttempt:

    # 09 / 12 / 2025 - 2:24 pm

    # Runtime -> 64ms - 93.53%
    # Memory -> 28.30 MB - 98.36%

    # this was all ME!!!! GETTING BETTER!!! nah but i did use the #2 hint from leetcode
    # but my struggle was in that first i thought about going through each match but that
    # definitely would be too slow, then i was like okay there is def a better way like
    # maybe starting one at start and one at end then moving inwards, but i couldn't wrap
    # my head around how we would increment / decrement pointers

    # but the hint said "Always move the pointer that points to the lower line." and then 
    # it made way more sense, like if we just start outside (becasue that has the greatest
    # distance), then keep track of a maxArea, we can just track the lower line as it
    # is the most defining of the area

    # so thats basically what i did in this, start out with two pointers, i & j, and a 
    # maxArea value, then while i < j, calculate current area, if greater than our maxArea,
    # update, then just increment / decrement our pointers based on the lower line.

    # really simple, but i had to think through it a bit. 

    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
        maxArea = 0

        while (i < j):
            curMax = (min(height[i], height[j])) * (j - i)
            if (curMax > maxArea):
                maxArea = curMax

            if height[i] > height[j]:
                j-=1
            else:
                i+=1

        return maxArea