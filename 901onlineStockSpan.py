# https://leetcode.com/problems/online-stock-span/
# medium

class firstAttempt:

    # 11 / 15 / 2025 - 1:34 pm

    # Did not work. 98 / 99 test cases. Time limit exceeded.

    # FUCK!!!!!

    # thought it was perfect but looking at some "worst" cases
    # it could be like O(n^2).

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        n = len(self.stack)
        self.stack.append(price)

        idx = n - 1

        while idx >= 0:
            if price < self.stack[idx]:
                break
            idx -= 1

        return n - idx

class monotonicStack:

    # i was so close!! kinda.

    # 11 / 15 / 2025 - 1:45 pm

    # Runtime -> 42 ms - 94.92%
    # Memory -> 22.79 MB - 72.33%

    # this approach just kind of changed out the while loop in mine for the monotonic stack
    # set up. i understand what its doing a lot better now.

    # so looking at the code below : 

    # they set up the stack as a list of tuples. where the first value of each tuple is the price,
    # then the second value is the span. so basically they initialize the span to 1, just because
    # each day is included as 1, even its its just one day. 

    # then they enter the loop, assuming the stack exists (so its past the first day), and they check
    # if the price is greater or equal to than the price at the top of the stack (the price from the 
    # previous day if hasn't been popped off yet), if so, they pop that off the stack, then take
    # the span from that day, and add it to the current span, and they do this until they reach
    # a price that is less than the most recent price in the stack. then after completing the while
    # loop, they append current price and span to the stack, then return the span.

    # the secret for this comes in the pop, because if you work your way backwards and just reference
    # the values without removing once you find the condition, you end up over adding the values.
    # so when you pop, the span of the following or future values will store the aggregate needed to complete the 
    # calculations for the next values.

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span