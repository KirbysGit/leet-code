# https://leetcode.com/problems/basic-calculator/
# hard

class firstAttempt:

    # 02 / 07 / 2026 - 4:05 pm

    # still working throuhg it right now. 
    # its def a struggle handling the parenthesis and knowing the order
    # of operators with that.
    # just had the lightbulb of PEMDAS, but we'll see if i can really
    # implement that.

    # right now just trying to figure out how to hanlde like
    # when to know to do each one. like you need to do substraction
    # before you add to stack.

    def calculate(self, s: str) -> int:

        operators = ["+", "-", "*", "/"]

        s = s.replace(" ", "")
        s = list(s)
        s.append(")")

        nums = []
        ops = []

        print(s)
        
        for char in s:
            if char == "(":
                continue
        
            if len(nums) == 2:
                print(nums)
                print(ops)
                while ops:
                    x = nums.pop()
                    y = nums.pop()
                    op = ops.pop()
                    nums.append(self.solve(x, y, op))

            if char in operators:
                ops.append(char)
            else:
                nums.append(int(char))

        return nums[0]
    

    def solve(self, x, y, op):
        if op == '+':
            return y + x
        elif op == '-':
            return y - x
        elif op == '*':
            return y * x
        else:
            return y / x


class secondAttempt:

    # 02 / 08 / 2026 - 11:19 pm
    
    # was drinking at superbowl party. wanna finish this shit, but need a git commit rn. 
    
    # working on it rn.

     # 02 / 09 / 2026 - 10:16 pm

    # we're back, almost 24 hours later, still working through this. shits ass.
    
    # this is where im at.

    # 11 / 49 test cases.

    # right now im not handling the negative signs like at all. and its just
    # so messy. like im just like symptom handling.

    # idea right now really is just to iterate through, recurse on parenthesis,
    # then handle operators and numbers as i would normally.

    operators = ["+", "-", "*", "/"]
    cur = 0

    def calculate(self, s: str) -> int:
        print("Cur Str : ", s)
        nums = []
        ops = []

        idx = 0
        n = len(s)

        while idx < n:
            if s[idx] == ")":
                self.cur = idx + 1
                break
                
            if s[idx] == " ":
                idx += 1
                continue

            if s[idx] == "(":
                add = self.calculate(s[idx + 1 : ])
                idx += (self.cur + 1)
                nums.append(add)
                continue

            if len(nums) == 2:
                while ops:
                    x = nums.pop()
                    y = nums.pop()
                    op = ops.pop()
                    nums.append(self.solve(x, y, op))
            
            if s[idx] in self.operators:
                ops.append(s[idx])
            else:
                nums.append(int(s[idx]))

            idx += 1

        
        while ops:
            x = nums.pop()
            y = nums.pop()
            op = ops.pop()
            nums.append(self.solve(x, y, op))

        return int("".join(map(str, nums)))
    

    def solve(self, x, y, op):
        if op == '+':
            return y + x
        elif op == '-':
            return y - x
        elif op == '*':
            return y * x
        else:
            return y / x

class thirdAttempt:

    # 02 / 10 / 2026 - 12:06 pm

    # FUCKKKKKK!!!! 

    # i didn't think about two digit numbers. like the case "1 - 11".

    # i handle it like 1 - 1 , 1, which doesn't work.

    # this is where im at, still just handling symptoms.

    def calculate(self, s: str) -> int:
        print("Cur Str : ", s)
        nums = []
        ops = []

        idx = 0
        n = len(s)

        while idx < n:
            if s[idx] == ")":
                self.cur = idx + 1
                break
                
            if s[idx] == " ":
                idx += 1
                continue

            if s[idx] == "(":
                add = self.calculate(s[idx + 1 : ])
                idx += (self.cur + 1)
                nums.append(add)
                print(add)
                continue

            if len(nums) == 2:
                while ops:
                    x = nums.pop()
                    y = nums.pop()
                    op = ops.pop()
                    nums.append(self.solve(x, y, op))
            
            if s[idx] in self.operators:
                ops.append(s[idx])
            else:
                toAdd = int(s[idx])
                if ops and not nums:
                    ops.pop()
                    toAdd *= -1
                nums.append(toAdd)

            print(nums)

            idx += 1

        if ops:
            if len(nums) == 2:
                x = nums.pop()
                y = nums.pop()
                op = ops.pop()
                nums.append(self.solve(x, y, op))
            else:
                ops.pop()
                nums.append(nums.pop() * -1)

        return int("".join(map(str, nums)))
    

    def solve(self, x, y, op):
        if op == '+':
            return y + x
        elif op == '-':
            return y - x
        elif op == '*':
            return y * x
        else:
            return y / x
    
class fourthAttempt:

    # 02 / 10 / 2026 - 7:09 pm 

    # 32 / 49 test cases.

    # running into same issue. restarted completely and running into issue with 
    # not handling double digits numbers. trying to find a work around but
    # i haven't gotten anything yet.

    operators = ['+', '-', '*', '/']
    steps = 0

    def calculate(self, s: str) -> int:
        
        if isinstance(s, str):
            expression = s.replace(" ", "")

        idx = 0
        stack = []

        while idx < len(expression):
            value = expression[idx]

            if value == '(':
                stack.append(self.calculate(expression[idx + 1 : ]))
                idx += self.steps + 1
            elif value == ')':
                self.steps = idx
                break
            else:
                if value in self.operators:
                    stack.append(value)
                else:
                    num = int(value)
                    if stack and isinstance(stack[-1], int):
                        tens = stack.pop()
                        num = (tens * 10) + num
                    if len(stack) == 1 and stack[0] == '-':
                        stack.pop()
                        num = num * -1 
                    stack.append(num)

            if len(stack) == 3:
                x = int(stack.pop())
                op = stack.pop()
                y = int(stack.pop())
                stack.append(self.solve(x, y, op))

            idx += 1

        if len(stack) > 1:
            return int(stack[1]) * -1
        return int(stack[0])
        
    def solve(self, x: int, y: int, op: char):
        if op == '+':
            return y + x
        elif op == '-':
            return y - x
        elif op == '*':
            return y * x
        else:
            return y / x
        
class fifthAttempt:

    # bro 🤣🤣🤣🤣🤣

    # this is so ass!!! i just put like an hour into this off where i was. 
    # i even used chatgpt for a second on handling PEMDAS. but i got to
    # a memory error with ...
    
    # 48 / 49 TEST CASES PASSED!!! 

    # i mean to be fair i've just been like specific as hell with my handling
    # like my brain starts smoking when i try to think about like a general
    # solution, like something that can handle multiple issues.

    # i'll probably use chatgpt to help me out because the memory error means
    # i'm just not popping quick enough and the array is like exponentially growing.

    # here is where i am at :

    operators = ["+", "-", "*", "/"]
    cur = 0

    precedence = {
        '+': 1, '-': 1, '*': 2, '/': 2
    }

    def calculate(self, s: str) -> int:
        nums = []
        ops = []

        idx = 0
        n = len(s)

        while idx < n:
            if s[idx] == ")":
                self.cur = idx + 1
                break
                
            if s[idx] == " ":
                idx += 1
                continue

            if s[idx] == "(":
                add = self.calculate(s[idx + 1 : ])
                idx += (self.cur + 1)
                nums.append(add)
                continue
            
            if s[idx] in self.operators:
                while ops and len(nums) >= 2 and self.precedence[ops[-1]] >= self.precedence[s[idx]]:
                    nums.append(self.solve(nums, ops))
                if ops and self.precedence[ops[-1]] >= self.precedence[s[idx]] and len(nums) == 1:
                    ops.pop()
                    x = nums.pop()
                    nums.append(x * -1)
                ops.append(s[idx])
            else:
                toAdd = int(s[idx])
                if ops and not nums:
                    ops.pop()
                    toAdd *= -1
                if nums and s[idx - 1].isdigit():
                    tens = nums.pop()
                    if tens > 0:
                        toAdd = (tens * 10) + toAdd
                    else:
                        toAdd = (tens * 10) - toAdd
                
                nums.append(toAdd)

            idx += 1

        if ops:
            if len(nums) == 2:
                nums.append(self.solve(nums, ops))
            else:
                nums.append(nums.pop() * -1)

        return int(nums[0])
    

    def solve(self, nums, ops):
        x = nums.pop()
        y = nums.pop()
        op = ops.pop()
        if op == '+':
            return y + x
        else:
            return y - x
    
class done:

    # 02 / 12 / 2026 - 11:49 am

    # whelp. i lost.

    # i had to use chatgpt. i mean it didn't really give me the answer but it kinda did.

    # i honestly don't think i would've gotten this approach though, i would've never
    # thought to use the sign as a separate variable.

    # basically the approach is a one pass solution, moving through, 

    # if the value is an open parenthesis, we push the result and sign onto the stack 
    # and reset for the sake of having a fresh state for the inner expression.

    # if the value is a closed parenthesis, we pop result and sign from stack and add
    # onto the result to get the final result after that expression.

    # if value is a plus or minus, we add onto result and update sign.

    # else if number just throw that guy onto the stack.

    # its so simple in hindsight but i was too far in with my approach to want to
    # break away and take a much simpler way.

    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = []

        s = s.replace(" ", "")

        for val in s:
            if val == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif val == ')':
                result += sign * number
                number = 0
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            elif val == '+':
                result += sign * number
                number = 0
                sign = 1
            elif val == '-':
                result += sign * number
                number = 0
                sign = -1
            else:
                number = number * 10 + int(val)

        result += sign * number

        return result