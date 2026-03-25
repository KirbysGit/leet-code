# https://leetcode.com/problems/invert-binary-tree/
# easy

class firstAttempt:

    # bro i got this like first try in 5 minutes. im the goat.

    # i mean the problem is really easy, but still, the way my code had zero errors (except for once when
    # i forgot to return the root but that doesn't count) and i typed it up in like 1 minutes.

    # proud of that tho!

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.18 MB - 95.39%

    # idea really is just to recurse nodes and swap left and right children.

    # here is the code :

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return

        left = root.left
        right = root.right

        root.left = right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root