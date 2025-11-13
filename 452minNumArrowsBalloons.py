# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# medium

class firstAttempt:

    # 11 / 13 / 2025 - 2:16 pm

    # Runtime -> 63 ms - 88.96%
    # Memory -> 51.22 MB - 92.45%

    # alright this is the same sort of thing as yesterday. i struggled to understand how to set it up
    # but i had the right idea coming through my first approach. with that two pointer with the 
    # sorted balloons. but basically, i was misunderstanding how to keep track of the left point
    # like if there was a set of balloons that were overlapping, but we were only tracking the right
    # value and our right value for one balloon was less than our left value for a balloon in the future
    # then how would we keep track of it.

    # the solution was similar to the one yesterday, we sort based on the end value because then we can 
    # always just fire up from the end value. basically identical set up as yesterday, except instead
    # of tracking non-overlapping, we are tracking overlapping intervals.

    # the main check with the if, is if the end of the previous balloon is before the start of the current
    # one then there is no overlap.

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        totalNum = len(points)

        points.sort(key=lambda x: x[1])

        front = 0
        arrows = 0

        for i in range(1, len(points)):
            if (points[front][1] < points[i][0]):
                front = i
                arrows += 1

        return arrows + 1