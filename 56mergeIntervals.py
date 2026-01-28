# https://leetcode.com/problems/merge-intervals/
# medium

class firstAttempt:

    # 01 / 28 / 2026 - 1:04 pm

    # im the goat.

    # got it pretty quickly!!! i feel theres a simpler way to do it but i gotta figure
    # that out. 

    # my idea was to first just move through the list and check if the end of the 
    # current interval is greater than or equal to the start of the next interval,
    # if so we can take it over and update our end. else we just add the current
    # interval to the output list.

    # i ran into one issue with the final value not being added, which i had in the 
    # last problem too, not sure how to control that, but i just added a final
    # "out.append([start, end])" outside of the loop and that covered it. 
    
    # then i ran into the issue if the range was overlapping completely like
    # with [1, 4] and [2, 3], and i was thinking how we could just skip
    # that completely by checking our current start and end.

    # this is how i did it :

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        out = []
        start = intervals[0][0]
        end = intervals[0][1]

        for idx in range(1, len(intervals)):
            if intervals[idx][0] >= start and intervals[idx][1] <= end:
                continue

            if intervals[idx][0] <= end:
                end = intervals[idx][1]
            else:
                out.append([start, end])
                start = intervals[idx][0]
                end = intervals[idx][1]
        
        out.append([start, end])

        return out