# https://leetcode.com/problems/simplify-path/description/
# medium

class firstAttempt:

    # 02 / 03 / 2026 - 12:39 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.49 MB - 13.56%

    # alright so this problem seemed pretty easy because it was.
    # in reality we're only really adjusting the list if we encounter a 
    # .. , because other than that, the /'s aren't being picked up if
    # we split based on them. and we just append the actualy strings
    # we find.

    # what i did was first off to get the char so we could set it up
    # in a stack, i split the string based on the /'s. then from there
    # iterate through the list, skipping if its a empty space or a 
    # single period. then if its the double period, just pop that last
    # element, then if anything else like a ... or a string, just
    # append it to the stack. then join the stack with the /'s and return!

    def simplifyPath(self, path: str) -> str:
        chars = path.split("/")

        stack = []

        for char in chars:
            if char == '' or char == '.':
                continue
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "/" + "/".join(stack)