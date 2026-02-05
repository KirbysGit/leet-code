# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# medium

class firstAttempt:

    # 02 / 05 / 2026 - 1:14 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 20.72 MB - 19.66%

    # alright i mean i thought of the solution pretty quickly, just ran into some small issues that
    # i wasn't really thinking about.
    
    # first off its like those problems i had to do in mr.meade's class, where like you keep track
    # of a stack and the last values in, then when its an operator, use the last two values.

    # so i set up a stack, and iterate through values, if its a number, just add it to the stack,
    # else, just deal with the operator based on the last two values and push the result back
    # onto the stack. 

    # only issue i ran into was how to handle the division because the rounding came out weird with
    # negatives vs positives.

    # here's the approach : 

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = set(["+", "-", "*", "/"])

        for alpha in tokens:
            if alpha in operators:
                x = int(stack.pop())
                y = int(stack.pop())
                if alpha == "+":
                    stack.append(x + y)
                elif alpha == "-":
                    stack.append(y - x)
                elif alpha == "*":
                    stack.append(x * y)
                else:
                    div = y / x
                    if div < 1 and div > -1:
                        stack.append(0)
                    else:
                        stack.append(div)
            else:
                stack.append(alpha)
        
        return int(stack[-1])

class anotherSolution:

    # 02 / 05 / 2026 - 1:20 pm

    # i just saw this an i don't think i've ever used this sort of thing before.

    stack = []
    operators = ['+', '-', '*', '/']
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case '+':
                        stack.append(a + b)
                    case '-':
                        stack.append(a - b)
                    case '*':
                        stack.append(a * b)
                    case '/':
                        stack.append(a / b)
    return stack[0]