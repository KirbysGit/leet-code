# https://leetcode.com/problems/valid-anagram/
# easy

class firstAttempt:

    # alright so i did this yesterday morning, but i haven't taken notes on it
    # yet so im using it for the problem today. i mean thats what i planned to do
    # anyways.

    # 1 / 19 / 2026 - 6:57 pm

    # Runtime -> 3 ms - 98.39%
    # Memory -> 19.48 MB - 19.20%

    # its basically like if the strings are anagrams of each other. which
    # basically just means like if it has the same amount of specific letters,
    # in different orders.

    # so all we need is to count the frequencys and compare them.

    def isAnagram(self, s: str, t: str) -> bool:

        word1 = Counter(s)
        word2 = Counter(t)

        if word1 != word2:
            return False
        
        return True