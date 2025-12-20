# https://leetcode.com/problems/valid-palindrome/
# easy

class firstAttempt:

    # 12 / 20 / 2025 - 2:22 pm

    # Runtime -> 7 ms - 82.76%
    # Memory -> 19.26 MB - 25.63%

    # pretty simple palindrome sort of thing, all we needed to do was 
    # just get rid of all the non-alphanumeric characters which i then did
    # then just return like a comparison of the string and the reversed string.
    
    # so basically, lower entire string, then iterate through it, checking if
    # char is alphanumeric, if so, add to list, else continue. then return
    # comparison of the list and reversed list (f == f[::-1]).

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f = []
        for char in list(s)
            if char.isalnum():
                f.append(char)
        
        return f == f[::-1]

class simplerSolution:

    # Runtime -> 3 ms - 91.77%

    # same sort of thing, just kind of does it in one line. basically,
    # lowers char per iteration, then joins it into a string, then returns.

    def isPalindrome(self, s: str) -> bool:
        f = ''.join(char.lower() for char in s if char.isalnum())
        return f==f[::-1]

    