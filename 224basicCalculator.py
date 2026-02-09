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