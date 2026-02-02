# https://leetcode.com/problems/valid-parentheses/
# easy

class firstAttempt:

    # 02 / 02 / 2026 - 2:22 pm <- heaven sent.

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.40 MB - 32.84%

    # it took me a while to get through this one honestly and i feel like there
    # has got to be a simpler way in code to do this because the way i was checking
    # the chars exactly felt kind of brute force in a sense rather than thinking
    # outside the box a bit more.

    # what i did was basically draw it out, and i noticed that when you bring
    # a parenthesis in, it has to match the last parenthesis in the stack. like
    # i push a '(' onto the stack. then when i bring on a ')', it has to match
    # and then they both pop off, and if there was any inner chars they would
    # already be popped off. 

    # so thats basically what i did except with a few extra checks to make sure
    # its closing parenthesis coming in, and that the popped char isn't a 
    # closing parenthesis. the focus is we need an OPEN and a CLOSE.

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and (char == ']' or char == ')' or char == '}'):
                front = stack.pop()
                if front == '{' and char != '}':
                    return False
                elif front == '[' and char != ']':
                    return False
                elif front == '(' and char != ')':
                    return False
                elif front == ')' or front == ']' or front == '}':
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True

class secondAttempt:

    # alright i just saw this in the solutions tab and it works really well too
    # what they did was just use a set mapping instead. which works pretty well
    # just to prevent the series of if statements that i have.

    # they initialize their stack, and their mappings, then iterate through the
    # chars in the string, checking if the current char is in the map, and if so,
    # if the mapping is not the same as the last char in the stack, return false.

    # if its not in the mapping, meaning if its an open parenthesis we push it
    # as the check of the mapping only refers to the keys.

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.30 MB - 44.60%
    
    # basically same in terms of complexity.

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                else:
                    stack.append(ch)

        return not stack