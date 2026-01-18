# https://leetcode.com/problems/word-pattern/
# easy

class firstAttempt:

    # 1 / 18 / 2026 - 1:13 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.47 MB - 6.03%

    # alright this is the same sort of idea as the last one, almost identical
    # approach, except its letters to words instead of letters to letters. 
    
    # same exact set up tho with two dictionaries, one for letters to words, and one for words to letters.

    # just checking if the keys already exist and if they do, checking if the values are the same.

    def wordPattern(self, pattern: str, s: str) -> bool:
        
        ltr_to_string = {}
        string_to_ltr = {}

        split = s.split()

        if len(split) != len(pattern):
            return False
        
        for idx in range(len(pattern)):

            if pattern[idx] in ltr_to_string and ltr_to_string[pattern[idx]] != split[idx]:
                return False
            if split[idx] in string_to_ltr and string_to_ltr[split[idx]] != pattern[idx]:
                return False
            
            ltr_to_string[pattern[idx]] = split[idx]
            string_to_ltr[split[idx]] = pattern[idx]
        
        return True