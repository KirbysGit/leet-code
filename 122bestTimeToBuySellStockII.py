# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# medium

class firstAttempt:

    # 11 / 25 / 2025 - 2:32 pm
    
    # Runtime -> 3 ms - 39.35%
    # Memory -> 18.98 MB - 29.45%

    # i found the answer in my notebook from a similar problem, didn't mean to though,
    # wanted to solve it on my own, but anyways, the approach is a bit confusing to me
    # as of right now, basically looking at the solution below.

    # we carry two values, hold and cash, for price in the array, we update the 
    # cash to be the max of the previous cash and the previous hold + price. and the
    # hold to be the max of the previous hold and the previous cash - price.

    def maxProfit(self, prices: List[int]) -> int:
        
        hold = float('-inf')
        cash = 0
        for price in prices:
            cash = max(cash, hold + price)
            hold = max(hold, cash - price)

        return cash

    def betterVariables(self, prices: List[int]) -> int:

        max_profit_without_stock = 0
        max_profit_with_stock = float('-inf')

        for price in prices:
            max_profit_without_stock = max(max_profit_without_stock, max_profit_with_stock + price)  # sell
            max_profit_with_stock = max(max_profit_with_stock, max_profit_without_stock - price)     # buy

        return max_profit_without_stock
