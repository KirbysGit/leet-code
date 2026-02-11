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