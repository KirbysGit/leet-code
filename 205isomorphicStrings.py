# https://leetcode.com/problems/isomorphic-strings/
# easy

class firstAttempt:

    # 1 / 17 / 2026 - 9:42 pm

    # 42 / 47 test cases passed.

    # in my mind i was like okay, the main thing we need to consider is if 
    # the values of each letter come out to the same. like if its "bbbb" and "aaaa"
    # if they're equal then they're isomorphic.

    # i did this through two counters between the strings, then sorting them in 
    # descending order, then comparing the values as we iterate through returning
    # false if there is any that isn't the same.

    # i found out this didn't work because it didn't consider the order of the letters.

    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sCount = Counter(s)
        tCount = Counter(t)
        
        sorted(sCount.items(), key=lambda x: x[1])
        sorted(tCount.items(), key=lambda x: x[1])

        for (k1, v1), (k2, v2) in zip(sCount.items(), tCount.items()):
            if v1 != v2:
                return False
        
        return True