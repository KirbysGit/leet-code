# https://leetcode.com/problems/insert-interval/
# medium

class firstAttempt:

    # 01 / 29 / 2026 - 1:36 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 21.28 MB - 39.57%

    # okay i was in the middle of thinking through how to do this, and then i realized
    # i could just use the merge intervals function from yesterday and all i had to do
    # was add the new interval before the sort and it works.

    # it does come out to O(n * log n) because of the sort, but its still pretty fast.
    
    # but because the array is already sorted, theres another way we can do it in O(n)
    # that i want to work through.

    # but this is the first attempt :

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)

        intervals.sort(key=lambda x:x[0])

        out = []
        
        for interval in intervals:
            if not out or interval[0] > out[-1][1]:
                out.append(interval)
            else:
                out[-1][1] = max(interval[1], out[-1][1])
            
        return out

class secondAttempt:

    # 01 / 29 / 2026 - 1:56 pm

    # yep im officially the goat.

    # Runtime -> 0 ms - 100.00%
    # Memory -> 21.61 MB - 11.69%

    # basically the idea really is just to prevent the usage of the sort considering
    # the array is already sorted. i had to handle a bunch of cases i wasn't really
    # thinking about. it probably can be cleaned up a bit, but shit mine works, and
    # thats what matters.

    # some of the cases i wasn't thinking about were :
    # - if the new interval is before the first interval
    # - if the new interval is after the last interval
    # - if the new interval is completely inside of an existing interval
    
    # other than that though it was pretty much the exact same set up as yesterdays.
    
    # literally just added 3 more if statements to handle the cases with a boolean flag
    # to help out.

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        out = []
        inserted = False

        for interval in intervals:
            if newInterval[0] < interval[0] and not inserted:
                out.append(newInterval)
                inserted = True
            if not out or interval[0] > out[-1][1]:
                out.append(interval)
                if newInterval[0] <= out[-1][1]:
                    out[-1][1] = max(newInterval[1], out[-1][1])
                    inserted = True
            else:
                out[-1][1] = max(interval[1], out[-1][1])

        if not inserted:
            out.append(newInterval)

        return out
