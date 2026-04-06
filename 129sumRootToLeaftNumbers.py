# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# medium

class imTheGoat:

    # 04 / 06 / 2026 - 2:12 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.48 MB - 19.13%

    # im the goat.

    # alright so this one i looked at last night because i just wanted to see what it 
    # was, and i look at it and solved it mentally pretty quickly, the only thing
    # i was a bit confused abovut what how to keep track of the sum, so i just did
    # a global variable.

    # idea was to iterate down the tree left shifting the values and adding the
    # current value to the sum, then if its a leaf node, add this sum to the total.

    # here's the code : 

    def __init__(self):
        self.final = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def forwards(current, new):
            return (current * 10) + new
        
        def recurse(root, current):
            if root.right == None and root.left == None:
                self.final += forwards(current, root.val)

            current = forwards(current, root.val)

            if root.left:
                recurse(root.left, current)
            if root.right:
                recurse(root.right, current)

            return
        
        recurse(root, 0)

        return self.final

class withoutGlobal:

    # alright i just saw this one in the solutions tab, def a better approach,
    # but still same idea. 

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(curr, num):
            if not curr:
                return 0

            num = num * 10 + curr.val
            if not curr.right and not curr.left:
                return num

            return dfs(curr.right, num) + dfs(curr.left, num)

        return dfs(root, 0)