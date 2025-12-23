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

class goingThrough150:

    # 12 / 23 / 2025 - 2:42 pm

    # Runtime -> 60 ms - 94.51%
    # Memory -> 27.75 MB - 95.43%

    # this was me coming back through the 150 review questions. dude im getting better at this!
    # i remembered doing it, but couldn't remember how to do it. had to write it out.

    # set it up like this, took me like 10 minutes still, but i did it!

    def maxArea(self, height: List[int]) -> int:
        
        front = 0
        back = len(height) - 1
        area = 0
        most = 0

        while front < back:
            area = min(height[front], height[back]) * (back - front)
            if area > most:
                most = area

            if height[front] <= height[back]:
                front += 1
            else:
                back -= 1
        
        return most