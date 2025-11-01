# https://leetcode.com/problems/domino-and-tromino-tiling/
# medium

class firstAttempt:

    # 11 / 01 / 2025 - 2:32 pm

    # Runtime -> 3 ms - 50.02%
    # Memory -> 17.88 MB - 65.18%

    # this one really was fucking with my brain. overall the "partial" concept is 
    # still really not making much sense, i was trying to use mr.gpt to help me 
    # understand it, but it just hasn't really clicked, like i get the idea of how
    # it keeps track of the overhangs of the trominos, but like i don't see myself
    # ever thinking of the problem like that. 

    # i've seen some other solutions that follow a similar set up but they still
    # are so foreign to me. 

    # so looking at the solution : 

    # first off, check if n <= 2, if so, lucky enough, the valuesa re the same, just return n.

    # then we move on, and initialize our dp and partial arrays, 1 indexed.

    # we set the 1st and 2nd index of dp to 1 and 2, then set the second value of the partial
    # to 1, as it represents the first case where a tromino could *start* to form an overhang.

    # now we iterate from 3 to n :
    # dp[i] represents the total number of full tilings for a 2 x i board.
    # partial[i] represents the number of half filled states that have one square hangin.

    # the recurrence:
    # dp[i] = dp[i - 1] + dp[i - 2] + 2 * partial[i - 1]
    # - dp[i - 1]: its like adding a vertical domino at the end of all dp[i - 1] boards.
    # - dp[i - 2]: its like adding two horizontal dominoes on top of all dp[i - 2] boards.
    # - 2 * partial[i - 1]: fill in the overhangs on either side.

    # then partial comes in with
    # partial[i] = partial[i - 1] + dp[i - 2]
    # this says taht each partial state can either extend a previous partial,
    # or come fro ma full dp[i - 2] bord with one new tromino overhang.

    # then we just return the dp[n].

    # WHAT THE FUCK IS THIS PROLBEM!!!


    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        partial = [0] * (n + 1)

        dp[1], dp[2] = 1, 2
        partial[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + 2 * partial[i - 1]
            partial[i] = partial[i - 1] + dp[i - 2]

        return (dp[n]) % (10**9 + 7)
    
class slightlySimpler:

    # this is the same sort of thing but without the partials.
    
    # i really just don't understand how we're expected to connect the dots to
    # get to this point, considering the crazy math behind it. 

    # idk im getting better but holy shit.

    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)

        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return (dp[n]) % (10**9 + 7)