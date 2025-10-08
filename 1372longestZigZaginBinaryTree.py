# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# medium

class firstAttempt:

    # 10 / 04 / 2025 - 3:13 pm

    # Runtime -> 69ms - 44.95%
    # Memory -> 32.99 - 85.76%

    # aight this might be the longest i've spent on one problem and i didn't even
    # get it, i had to use chatgpt completely, i had it kind of set up in my head
    # but man just walking through the recursive logic fucks up my brain
    
    # like trying to wrap my head around the nests really was overwhelming me, 
    # but i definitely was on the right track but i just couldn't get the maxPath
    # logic to be passed correctly, i was trying too much to fit specific 
    # examples and i wasn't really generalizing well.

    # the solution i landed on with gpt from my approach is shown below, its pretty
    # slow overall.
    
    # basically, global variable for maxPath

    # zigZag which is just dfs, but base case, then update the current maxPath,

    # then if direction is left, we go right, and had 1 to length, and thne
    # left and set length to 1

    # then if direction is right, we go left, and had 1 to length, and then
    # right and set length to 1

    # then we just call the function on the left and right and return the global.

    # still really weird to me, recursion blows honestly, but ill keep getting better.

    def __init__(self):
        self.maxPath = 0

    def zigZag(self, node, direction, length):
        if not node:
            return

        self.maxPath = max(self.maxPath, length)

        if direction == "left":
            self.zigZag(node.right, "right", length + 1)
            self.zigZag(node.left, "left", 1)
        elif direction == "right":
            self.zigZag(node.left, "left", length + 1)
            self.zigZag(node.right, "right", 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.zigZag(root.left, "left", 1)
        self.zigZag(root.right, "right", 1)

        return self.maxPath