# https://leetcode.com/problems/asteroid-collision/
# medium

class firstAttempt:

    # imma be honest i had like 10 different "first attempts", i really couldn't 
    # get around some specific things, but chatgpt gave me some hints like using
    # a flag for the while loop instead of just trying to find a perfect long
    # ass condition which is what i was doing previously.

    # 09 / 22 / 2025 - 4:21 pm

    # Runtime -> 7 ms - 59.61%
    # Memory -> 18.61 MB - 96.57%

    # idea here is to use a stack.
    # iterate through the asteroids, if stack is empty, or last asteroid in stack
    # is negative, or current asteroid is positive, we can just add it to the stack.
    # else, we set a flag to true for our while loop, and while len of stack > 0,
    # the last asteroid in stack is positive and the flag is true.

    # we can check
    # if last asteroid less than current asteroid magnitude, pop last asteroid.
    # if last asteroid is equal to current asteroid magnitude, pop last asteroid and set flag to false.
    # if last asteroid is greater than current asteroid magnitude, set flag to false.

    # then if flag still true at the end of the while loop, add cur asteroid to stack.

    # pretty simple, but kinda slow.
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            if len(stack) == 0 or stack[-1] < 0 or ast > 0:
                stack.append(ast)
            else:
                cur = True
                while len(stack) > 0 and stack[-1] > 0 and cur == True:
                    if stack[-1] < abs(ast):
                        stack.pop()
                    elif stack[-1] == abs(ast):
                        stack.pop()
                        cur = False
                    else:
                        cur = False
                
                if cur == True:
                    stack.append(ast)
                    
        return stack