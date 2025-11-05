# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# medium

class firstAttempt:

    # 11 / 04 / 2025 - 1:50 pm

    # Runtime -> 87 ms - 94.06%
    # Memory -> 23.43 MB - 79.71%

    # okay this one is a bit different, i went into i thinking about how to 
    # set up our dp array with the 2D grid, but its much simpler than that at the end of the
    # day considering there is only really two states that need to be kept track of.

    # i still am a bit confused on the logic behind the states, like understand how it
    # works, but the aggregation of the states always being optimized is whats throwing me off.

    # the set up is really just to intiialize two values:

    # cash and hold. cash at 0, hold at -infinity.
    # then we iterate through the prices, per price we
    # update the cash based on the previous cash, and the previous hold + price - fee.
    # what that is doing is we are checking the available profit if we were to sell at the current price
    # based on our current hold.
    # then we update the hold based on the previous cash and the current price. this basically
    # tells us, if we were to buy at the current price, what is the best we could do with our current cash.

    # finally we just return the cash which holds the best profit we could have.

    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        hold = float('-inf')
        cash = 0

        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash