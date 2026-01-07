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