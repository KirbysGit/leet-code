# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy

class firstAttempt:

    # 11 / 24 / 2025 - 2:12 pm

    # Runtime -> 17 ms - 97.65%
    # Memory -> 26.76 MB - 94.63%

    # alright i tried a bunch with like a two pointer approach but i wasn't
    # properly handling like if the best profit wasnt even, like say they
    # were both on the front side of the array, then it wouldn't work.

    # but i had to use chatGPT. :( . but it recommended just like tracking
    # one minPrice, and i was like oh okay, then i got it, i feel like i 
    # did a similar problem to this already, but i get the approach.
    
    # basically, we just iterate through the prices, and at each
    # price we check if current price is less tha nthe minPrice, if so
    # update the min price, then we check the current profit and see if
    # its more than our maxProfit and if so update maxProfit. then we
    # return the maxProfit at the end. it works because we're not tracking
    # the past values if they weren't our minprice which is all i was trying
    # to do.

    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = 10001
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            
            curProfit = price - minPrice
            if curProfit > maxProfit:
                maxProfit = curProfit

        return maxProfit