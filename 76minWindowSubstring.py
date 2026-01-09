# https://leetcode.com/problems/minimum-window-substring/
# hard

class firstAttempt:
    
    # 1 / 7 / 2026 - 2:14 pm

    # this is how you know i didn't use ai. 

    # Runtime -> 3639 ms - 5.01%
    # Memory -> 20.89 MB - 10.94%
    
    # yea so i did it all by myself but theres some room for improvement.

    # basically my approach was a normal sliding window, like move to the right, 
    # if condition met, then bring left pointer in until not met. then continue
    # moving to the right.

    # coming back tmrw lets focus on how we can speed it up.

    def minWindow(self, s: str, t: str) -> str:
        lenS = len(s)
        lenT = len(t)

        if lenS < lenT:
            return ""
        if s == t:
            return t

        counts = {}
        cur = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1
        
        for char in s:
            cur[char] = cur.get(char, 0) + 1

        if not (all(cur.get(k, 0) >= v for k, v in counts.items())):
            return ""
        
        cur = {}
        tmp = []
        best = list(s)

        for char in s:
            # add cur char to our tmp list & counter dict.
            tmp.append(char)
            cur[char] = cur.get(char, 0) + 1
            
            # if still not same length as t, continue.
            if len(tmp) < lenT:
                continue

            # if t is subset of our tmp.
            while all(cur.get(k, 0) >= v for k, v in counts.items()):
                if len(best) > len(tmp):
                    best = tmp.copy()
                ltr = tmp.pop(0)
                cur[ltr] = cur.get(ltr, 0) - 1
                if cur[ltr] == 0:
                    del cur[ltr]
            
        return "".join(best)

class gptAssist:

    # 1 / 9 / 2026 - 12:03 am

    # Runtime -> 61 ms - 81.93%
    # Memory -> 19.99 MB - 5.01%
    
    # alright so this takes a pretty similar approach except, instead of 
    # tracking like the two dictionaries equivalency, its more of two pointer method with
    # a counter for if the chars have been formed already.

    # starts out with setting up the dictionary for the chars in t, so we know the counts per char.
    
    # then we set some variables to help us loop through.

    # looping through we update our cur window with the char at right pointer, then check if
    # the char count in the cur window is equal to the count in our t dictionary.

    # while our condition for formed is true, we check if window is better than our best window,
    # if so update it, else we just basically move the left pointer to the right until the condition
    # that the chars in the cur window are less than the count in our t dictionary.

    # this left pointer moving in allows us to find the smallest window while the condition is still true.

    # code below :

    def minWindow(self, s: str, t: str) -> str:

        # setting up t dictionary for what we need.
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        # setting up required for our comparator to know if we have all chars we need.
        required = len(set)

        # setting up some basic variables.
        left = 0
        right = 0
        formed = 0
        window = {}

        best_len = float('inf')
        best_start = 0

        # while window is less than len of s.
        while right < len(s):
            
            # grab char at right pointer and add it to our window dict.
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # if the char is in our need dict and the count of the char is now equal, increment our formed counter.
            if char in need and window[char] == need[char]:
                formed += 1

            # while formed counter is equal to required, check if window is better than our best window.
            while formed == required:
                
                # if so, update our best window variables.
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                
                # grab char at left pointer and decrement it from our window dict.
                left_char = s[left]
                window[left_char] -= 1

                # if char is in need dict and the count of the char is now less than the count in need dict, decrement formed.
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                # increment left pointer to slide window right.
                left += 1
            
            # increment right pointer to slide window right.
            right += 1

        # if best len is still inf, return empty string, else return the best window.
        if best_len == float('inf'):
            return ""
        else:
            return s[best_start : best_start + best_len]

