# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# easy

class firstAttempt:

    # 09 / 29 / 2025 - 2:45 pm 

    # Runtime -> 3 ms - 30.84%
    # Memory -> 19.27 MB - 7.53%

    # had to use chatgpt completely, couldn't understand how to set it up, because
    # like how do we return up the tree after reaching the end other than using a 
    # series of pointers. so i wasn't undersatnding, then it explained a recursive
    # approach, but it didn't really make sense to me. so i had to go to mr.gpt to 
    # work it out and landed upon this.

    # first check is like, if the current node doesn't exist, we're at bottom.

    # then we recursively call the function on the left and right nodes, 
    # the function asks the same question of the children : 
    # "Hey left child, what's your max depth?"
    # "Hey right child, what's your max depth?"
    #  These calls return the int depths of each subtree.

    # then the return statement is 1 + the max depth of the left and right subtrees.
    # really got to understand this and put some time in.

    # all solutions are variations of this, just different ways of implementing it.
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
