# https://leetcode.com/problems/longest-common-prefix/
# easy

class firstAttempt:

    # 12 / 12 / 2025 - 1:35 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.72 MB - 78.15%

    # alright i had to use google a bit because idk i assumed there was a function or like
    # line that you could use that i didn't know about that would make this like a one liner solution.

    # i was thinking like that because i feel like getting the idx of one word then iterating through
    # the rest of the words, for long words with similar prefixes would be too slow. but i guess thats
    # the solution. 

    # the solution is basically that tho, take the first ltr of the first word of the list, then 
    # iterate through the rest of the words and checking if the current letter is the same as the first letter.
    # then we break if we find a letter that is different or we reach the end of the word.

    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = []
        idx = 0

        while idx < len(strs[0]):
            ltr = strs[0][idx]
            for word in strs:
                if idx >= len(word) or word[idx] != ltr:
                    return "".join(prefix)
            prefix.append(ltr)
            idx += 1

        return "".join(prefix)
    