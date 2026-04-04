# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# medium

class firstAttempt:

    # 04 / 04 / 2026 - 3:29 pm

    # yep im the goat.

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.67 MB - 28.63%
    
    # i thought this problem was boutta take me forever. 

    # all i did was draw it out, thinking about how i can connect the nodes
    # that like works like a DFS but works by always moving the left node over
    # to the right side, and propelry displacing the right node.

    # the idea was to focus on the left node, as the right nodes can just
    # be connected like in a linked list, so per recursion, check the root to
    # see if ti has a left node, if so, save the right node
    # with some tmp value, then move the left node to the right, clear the
    # left node, then you need to go through all the values on the right node
    # to handle the case where the left node has children in the right subtree
    # so then recurse down that and connect the last right node of our left node
    # to the right node we saved, then recurse the right node.

    # sounds like a lot but its pretty simple when looking at it.

    # here's the code : 

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def recurse(root):
            if not root:
                return

            if root.left:
                tmp = root.right
                root.right = root.left
                root.left = None
                head = root.right
                while head.right:
                    head = head.right
                head.right = tmp

            recurse(root.right)
        
        recurse(root)