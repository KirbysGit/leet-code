# https://leetcode.com/problems/same-tree/
# easy

class firstAttempt:

    # 03 / 18 / 2026 - 10:41 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.36 MB - 62.31%

    # first question back from my hiatus! amazing to be back! 

    # my brain was really working on this problem. i mean it took me like 30 minutes
    # just because i didn't really get how to set it up. 

    # but i remembered like bfs and dfs, and the only thing was really just to check
    # the current state of each step and see if it breaks.

    # so thats what i was trying to do, but its so weird because the pattern
    # of the recursion is like how do we order it, i remembered its kind of 
    # like this :

    # base case
    # recurse case (in this case left and right)
    # return if it makes it here

    # so i did that basically, but i needed to handle the None, because they
    # technically don't have vals, so i did it this way.
    
    # super chill!

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p and not q:
            return False
        elif q and not p:
            return False
        elif p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right