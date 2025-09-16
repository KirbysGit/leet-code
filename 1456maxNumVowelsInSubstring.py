# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# medium

class firstAttempt:

    # 09 / 15 / 2025 - 5:15 pm

    # Runtime -> 67 ms - 84.17%
    # Memory -> 17.96 MB - 87.90%

    # alright this was without chatGPT, but this is almost identical to what i did yesterday
    # with the window, but i kept running into issues, i tried with a for loop but i don't
    # understand them as well with like setting idx's for values.

    # but idea here is have set of VOWELS (i just set it to a set which is way faster than 
    # just 'aeiou'). 

    #  we use front and back pointers for the window. we grab the initial window count with
    # that first while loop, then we set the max to that window count, then from there we
    # start sliding the window, with a couple of variables to keep track of if
    # we lost or gained a vowel, then we update the window count, and if greater than max
    # we update then slide the window.

    VOWELS = set('aeiou')

    def maxVowels(self, s: str, k: int) -> int:
        front = 0
        back = k
        idx = 0
        window_count = 0
        
        while (front + idx < back):
            if s[front + idx] in VOWELS:
                window_count+=1

            idx+=1
        
        max = window_count

        while (back < len(s)):
            lost = 0
            gained = 0

            if s[front] in VOWELS:
                lost = 1
            if s[back] in VOWELS:
                gained = 1

            window_count = window_count - lost + gained

            if (window_count > max):
                max = window_count
            
            front+=1
            back+=1

        return max

class enumerateStrat:

    # just saw this in the solutions tab, pretty similar to my idea with for loops, super smart
    # didn't know about enumerate, but basically same strat just using enumerate, its a bit 
    # faster too for some reason

    # same sort of thing, initial window, slide window, but also this approach gets rid of
    # my "loss" instead of doing that just if front is a vowel and back is not, we decrement
    # if front is not a vowel and back is, we increment

    # same apporach, better set up

    # Runtime -> 35 ms - 99.02%
    # Memory -> 17.93 MB - 87.90%

    VOWELS = set('aeiou')
    def maxVowels(self, s: str, k: int) -> int:
        currVow = 0
        for i in s[:k]:
            if i in VOWELS:
                currVow+=1

        maxVow = currVow

        for i, c in enumerate(s[k:]):
            if s[i] in VOWELS:
                if c not in VOWELS:
                    currVow -= 1
            else:
                if c in VOWELS:
                    currVow += 1
                    if maxVow < currVow:
                        maxVow = currVow

        return maxVow