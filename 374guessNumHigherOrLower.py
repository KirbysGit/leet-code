# https://leetcode.com/problems/guess-number-higher-or-lower/
# easy

class firstAttempt: 

    # 10 / 23 / 2025 - 2:09 pm

    # Runtime -> 35 ms - 73.33%
    # Memory -> 17.86 MB - 29.19%

    # took me a bit, simple idea, i keep thinking of that one interview with that 
    # millionaire guy, where you guess the number and he says higher or lower. but
    # with that i was struggling with like, handling the proper way to handle
    # decimals with it?

    # the idea is simple, but the implementation has some nitpicky stuff.

    # here's what i did : 

    # code seems overly complex now just looking at it.

    # start off with initial guess, if its 0, then return it.
    # else, start off the binary search, updating the guess based on the result,
    # if higher then increment by half the number, if lower then 
    # decrement by half the number. ran into some issues with decimals and it 
    # would go on forever so i didn't want to let that keep happening.

    def guessNumber(self, n: int) -> int:
        if (guess(n) == 0):
            return n

        n = n / 2
        myGuess = math.floor(n)
        attempt = guess(myGuess)
        
        while attempt != 0:
            if attempt == -1:
                n = n - n/2
                myGuess = myGuess - math.ceil(n)
            elif attempt == 1:
                n = n + n/2
                myGuess = myGuess + math.ceil(n)

            attempt = guess(myGuess)

        return int(myGuess)

class cleanerAttempt:

    # found it in solutions, simpler, but
    # i think its same time, maybe slightly better memory.

    def guessNumber(self, n: int) -> int:
        lo,hi = 1,n
        while lo <= hi: 
            mid = (lo+hi)//2
            if guess(mid) == 0: 
                return mid
            elif guess(mid) > 0:
                lo = mid + 1
            else: 
                hi = mid - 1

    # this approach is gas tho, i saw it and was like woah.
    # but start with a two pointer kind of thing (not really), but
    # while the values are less than or equal to each other, we keep
    # going through the middle, then we update the pointers.

    # if guess with mid val is 0, return that. else if 1, 
    # bring up low. if less than 1, bring down high. 