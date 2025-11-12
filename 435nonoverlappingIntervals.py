# https://leetcode.com/problems/non-overlapping-intervals/
# medium

class firstAttempt:

    # 11 / 12 / 2025 - 1:22 pm

    # Runtime -> 77 ms - 67.27%
    # Memory -> 51.43 MB - 21.87%

    # alright i got really close with this one but couldn't figure out where i was
    # going wrong. so like i got pretty much what i have right now, except i had it 
    # organized slightly differently in terms of reversed conditions, and then 
    # i was like okay how do i get the minimum number of intervals to remove, and 
    # idk why but i was like oh shit i can't use a sort. which makes no sense
    # but then i realized i could, and the only issue was just how i was sorting it
    
    # i was doing the default sort which just made it so the intervals were sorted
    # by the first value. but i needed to sort by  the second value to preserve the most
    # similar order.

    # the solution is below.

    # basically, sort with the lambda function. then for value in our intervals,
    # if the second value in the first interval is less than or equal to the first value
    # in the second interval, then we increment the front pointer. else we increment the
    # count as it means we need to remove it because they are overlapping.

    # then we return that bad boy and BAM!!!

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        count = 0
        front = 0

        for idx in range(len(intervals) - 1):
            if intervals[front][1] <= intervals[idx + 1][0]:
                front = idx + 1
            else:
                count += 1

        return count