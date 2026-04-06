# https://leetcode.com/problems/path-sum/
# easy

class worksButABitCodeHeavy:
    
    # 04 / 05 / 2026 - 8:57 pm

    # easter!!! he  has  risen!!!!

    # Runtime -> 0 ms - 100.00%
    # Memory -> 20.29 MB - 39.45%

    # alright so this one actually took me a bit, maybe like 30 minutes, just because i couldn't figure out how
    # to have the return True carry up to the top of the return statements.

    # it was an easy approach tho, like just iterate down, carry the current sum, then if its a leaf node
    # and the sum is equal to the target sum, then return True.

    # the code was weird, jsut needed to recurse with a proper return statement.

    # here's the code : 

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        def recurse(root, current, targetSum):
            if root.left is None and root.right is None:
                current = current + root.val
                if current == targetSum:
                    return True
                else:
                    return False

            left, right = False, False

            if root.left:
                left = recurse(root.left, root.val + current, targetSum)
            if root.right:
                right = recurse(root.right, root.val + current, targetSum)
            
            return left or right

        return recurse(root, 0, targetSum)

    # def a bit overdone, much simpler solutions exist.

class wayyyySimpler:

    # 04 / 05 / 2026 - 9:00 pm

    # i saw this in the solutions tab.

    # definitely less code, but same approach.

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        if not root.left and not root.right:
            return targetSum - root.val == 0

        targetSum -= root.val

    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)