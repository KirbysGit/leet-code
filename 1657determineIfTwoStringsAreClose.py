# https://leetcode.com/problems/determine-if-two-strings-are-close/
# medium

class firstAttempt:

    # 09 / 19 / 2025 - 3:48 pm

    # Runtime -> 162 ms - 24.37%
    # Memory -> 19.52 MB - 7.82%

    # pretty shit solution which shows that it was mainly me. but i still used chatgpt
    # because i was pretty lost on some of the syntax, but just looking at the problem
    # i had a pretty good idea we didn't really need to worry about the actual
    # movements but more of the availability of the letters and how to compare them.

    # so my idea is, initial check for lengthm

    # then initialize the count dictionies for each word, then count frequency of each
    # letter per word. 

    # then initialize the values to a list, and then convert the keys to a set
    # then we check if the sets are the same, and then if the sorted lists are the same
    # if so, return true, else, false.

    # honestly, just looking at this solution it seems very long and unncessary but i got
    # to think through some of the steps regarding how we can optimize.

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        countWord1 = {}
        countWord2 = {}

        for char in list(word1):
            countWord1[char] = countWord1.get(char, 0) + 1

        for char in list(word2):
            countWord2[char] = countWord2.get(char, 0) + 1
        
        numList1 = list(countWord1.values())
        numList2 = list(countWord2.values())

        charList1 = set(list(countWord1.keys()))
        charList2 = set(list(countWord2.keys()))
        
        if (charList1 == charList2) and sorted(numList1) == sorted(numList2):
            return True

        return False

class usingCounter:
    
    # Runtime -> 87 ms - 67.56%
    # Memory -> 18.03 MB - 93.31%
    
    # alright so this was how chatGPt said to speed it up, i didn't know about Counter
    # so this kind of solved the problem way simpler, same sort of idea but just 
    # saves a lot of time and memory

    # basically the Counter takes frequency of each letter and stores it in a dictionary
    # then we check if keys are the same, if not return false, then we check
    # if the values are the same, if so return true, else false.

    from collections import Counter

    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        if c1.keys() != c2.keys():
            return False
        
        return Counter(c1.values()) == Counter(c2.values())

class evenSimpler:

    # saw this one in solutions tab.

    # what its doing is checking if the sets of word1 and word2 are the same, meanining they have
    # the same letters, and if not return false. but if they do, we take the counter per word,
    # then sort of those values, and compare if they're the same.

    # pretty smart guy

    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())
        
        return freq1 == freq2