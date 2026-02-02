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

class secondAttmept:

    # 01 / 30 / 2026 - 4:01 pm

    # im in the process of going through this again with the Top Interview 150 list.
    # but im forgetting how to do it.

    # im not thinking about it clearly and i don't want to cheat to re-understand it.

    # i'll give myself time to think.

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[1])

        arrows = 0 

        start = points[0][0]
        end = points[0][1]

        print(points)

        for balloon in points:
            if end < balloon[0]:
                end = balloon[1]
                arrows += 1

            start = balloon[0]

        return arrows

class thirdAttempt:

    # post gasparillia. 

    # im the goat!!!

    # 02 / 01 / 2026 - 7:38 pm

    # Runtime -> 86 ms - 52.14%
    # Memory -> 53.52 MB - 29.17%

    # before dippping i really couldn't understand where i was going wrong. and honestly
    # i still don't fully understand what i did, i was like okay so if we are sorting
    # by the back value, then we only really need to check if the end of of the previous
    # balloon is before the start of the current balloon, then we can just increment the
    # back value and decrement the arrows based on the overlap.

    # idek what i just typed, shit took me like 10 minutes to get this code right.

    # just like if end of previous is overlapping with start of current, decrement arrows
    # else, move the "previous" value up.

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[1])

        arrows = len(points)

        overlap = points[0][1]

        for idx in range(0, len(points)):
            if points[idx][0] <= overlap:
                arrows -= 1
            else:
                overlap = points[idx][1]

        return arrows + 1

class goatStatus:

    # 02 / 01 / 2026 - 7:42 pm

    # Runtime -> 59 ms - 93.56%
    # Memory -> 53.48 MB - 41.89%

    # i looked at my other attempt, and was like okay if we instead increment the arrows
    # based on a lack of overlap, we don't need a separate else statement to handle
    # moving the back value up.

    # also, i forgot because im using an idx now i don't have to do the first index again.

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[1])

        arrows = 0

        overlap = points[0][1]

        for idx in range(1, len(points)):
            if points[idx][0] > overlap:
                arrows += 1
                overlap = points[idx][1]

        return arrows + 1