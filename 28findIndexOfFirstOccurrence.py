# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# easy

class firstAttempt:

    # 12 / 17 / 2025 - 2:31 pm

    # Runtime -> 7 ms - 2.03%
    # Memory -> 18.03 MB - 13.14%

    # YIKES!!!!

    # idk i was trying to do it with like a slice, but i don't know how to set it up.

    # so i did a pretty brute force but it works!

    # basically tries every word in every position, O(n^2) time complexity.

    def strStr(self, haystack: str, needle: str) -> int:
        
        front = 0
        i = 0
        j = 0
        n = len(needle)
        m = len(haystack)

        while i < m:
            if haystack[i] == needle[j]:
                print(i, j)
                j += 1
                if j >= n:
                    return i - n + 1
                
                i += 1
            else:
                front += 1
                i = front
                j = 0

        return -1

class faster:

    # 12 / 17 / 2025 - 2:34 pm

    # i was just thinking like why it would take so long, because it could go O(n^2) hypothetically on
    # words that don't have a solution.

    # so just adding this to the top of our last one we got a 0 ms run, but i don't think thats accurate.

    if needle not in haystack:
            return -1 

class fastest:

    # 12 / 17 / 2025 - 2:35 pm

    # this seems to be the fastest, and also simplest in terms of code. but like i didn't even
    # know find() existed.

    # insane.

    # im guessing find jsut returns first index of the first occurrence of the needle in the haystack.
    # so if we don't find it, it returns -1.

    # so we just return the result of find() and we're good to go.

    def strStr(self, haystack: str, needle: str) -> int:
        x=haystack.find(needle)
        return x