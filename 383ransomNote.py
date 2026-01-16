# https://leetcode.com/problems/ransom-note/
# easy

class firstAttempt:

    # 1 / 16 / 2026 - 1:19 pm

    # Runtime -> 23 ms - 50.26%
    # Memory -> 19.63 MB - 12.59%

    # alright i understood how i wanted to do the problem immediately but i wasn't really
    # sure how to implement it with dictionaries? like i just wanted to do if like
    # dictionary of ransomNote was in dictionary of magazine, but theres not a super
    # easy way to do that.

    # so i set it up with two for loops to create two hashmaps for the two strings.
    # then just checked if per char that it was in M or the count was lower than the
    # count in R, if so return false.

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        countM = {}
        countR = {}

        for char in magazine:
            countM[char] = countM.get(char, 0) + 1
        
        for char in ransomNote:
            countR[char] = countR.get(char, 0) + 1

        for c in countR:
            if c not in countM or countM[c] < countR[c]:
                return False
            
        return True


class secondAttempt:

    # 1 / 16 / 2026 - 1:22 pm

    # Runtime -> 22 ms - 52.45%
    # Memory -> 19.72 MB - 6.12%

    # this is basically the same thing except we only use 2 loops rather than 3,
    # and as we're iterating through the ransomNote string we're just checking if
    # the char is in the magazine by checking if the count is 0, if so we return false.
    # else we just decrement the count of that char in the magazine.

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    countM = {}
    countR = {}

    for char in magazine:
        countM[char] = countM.get(char, 0) + 1
    
    for char in ransomNote:
        if countM.get(char, 0) == 0:
            return False
        else:
            countM[char] -= 1
    
    return True
            
class counterFaster:
    
    # 1 / 16 / 2026 - 1:24 pm

    # this uses Counter from collections which just creates the hashmaps for us.
    # then we check if the ransomNote counter is less than or equal to the magazine counter.

    mc = Counter(magazine)
    rc = Counter(ransomNote)

    # the <= basically behaves like the less than or equal to operator, but goes per key.

    return rc <= mc