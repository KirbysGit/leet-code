# https://leetcode.com/problems/length-of-last-word/
# easy

class firstAttempt:

    # 12 / 11 / 2025 - 1:29 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.70 MB - 60.50%

    # my mentality was like okay, how can we move backwards and just stop when we run into
    # a space.

    # ran into issue with how we slice the string if we get to the first index, as we were slicing
    # off the first character.

    # so we slice the string from i:n if we make it to first index, otherwise, we slice from
    # i+1:n. and return the length of that.

    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()
        n = len(s)
        i = n - 1

        while i > 0:
            if s[i] == " ":
                return len(s[i+1:n])
            
            i -= 1
        
        return len(s[i:n])
        