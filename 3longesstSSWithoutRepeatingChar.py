# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# medium

class firstAttempt:

    # 1 / 3 / 2026 - 1:50 pm

    # Runtime -> 31 ms - 18.72%
    # Memory -> 17.44 MB - 83.15%

    # alright so i didn't use gpt, but its obviously very slow. but my goal was like
    # basically similar to the problem i did yesterday with the sliding window where we
    # have like a condition where we move one side of the window up, while continuously
    # moving the other side of the window up. 

    # and thats basically what i did. just like two conditions, one is just expanding list
    # other is just shrinking it to meet condition.

    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = []
        window = 0

        for char in s:
            if char not in seen:
                seen.append(char)
                window = max(window, len(seen))
            else:
                while char in seen:
                    seen.pop(0)
                seen.append(char)

        return window

class faster:

    # 1 / 3 / 2026 - 2:06 pm

    # Runtime -> 19 ms - 54.23%
    # Memory -> 17.29 MB - 94.59%

    # i used gpt because the solutions in the solution tab were overcomplicated i felt.
    # but what we do basically from our last solution is, use a set for membership, and get
    # rid of extra "if x in seen" check.

    # and then we use a front and back pointer, but it could be done the same sort of way.

    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        best = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best, right - left + 1)

        return best