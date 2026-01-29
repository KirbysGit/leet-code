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