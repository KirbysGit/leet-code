# https://leetcode.com/problems/merge-strings-alternately/
# easy

class firstAttempt:
    # 09 / 03 / 2025 - 2:40pm

    # Runtime -> 45 ms - 13.07%
    # Memory -> 17.86 MB - 33.81%

    # Idea is two have two pointers iterate through each string while less than the length of the string.
    # While iterating, add the character to the final string.
    # Return the final string.

    # string concat in loop
    # the time is slower because of many reallocations / copies
    # the memory is higher because it creates many intermediate strings

    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1 = len(word1)
        len2 = len(word2)
        final = ""
        i = 0
        j = 0

        while i < len1 or j < len2:
            if(i < len(word1)):
                final += word1[i]
                i+=1
            if(j < len(word2)):
                final += word2[j]
                j+=1

        return final
    

class optimizedTime:
    # Runtime -> 26ms - 98.34%
    # Memory -> 17.90 - 8.46%

    # Idea is to use a list to store the characters and then join them together.
    # Return the final string.

    # append chars -> join
    # time is faster because list appends are cheap, and one join.
    # memory is okay, you hold a list with m + n single-char strings plus the final string

    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = j = 0
        m, n = len(word1), len(word2)

        while i < m or j < n:
            if i < m:
                res.append(word1[i]); i += 1
            if j < n:
                res.append(word2[j]); j += 1

        return ''.join(res)
    
class optimizedMemory:

    # Runtime -> 41ms - 36.76%
    # Memory -> 17.60 MB - 94.93%

    # Starts out same, initialize, but instead of just iterating through both strings, iterate through one and then the other.
    # Then append the remaining characters from the other string.
    # Return the final string.

    # appending the two slices at the end reduces loop work, but each slice is a new string copy.
    # we're appending chunks instead of singel characters.

    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        result.append(word1[i:])
        result.append(word2[j:])
        
        return ("").join(result)