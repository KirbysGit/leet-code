# https://leetcode.com/problems/count-complete-tree-nodes/
# easy

class tryingToUnderstand:

    # 04 / 13 / 2026 - 10:46 pm

    # bro this problem is fucking insane.

    # it says its an easy, we need it to run in less than O(n) time.

    # we're given a tree that may not be full, and we need to find hte number of nodes.

    # without O(n) im lost bro. 

    # im mad as fuck right now too so imma stop this shit.

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = root
        right = root
        
        left_depth = 1
        right_depth = 1

        while left.left:
            left_depth += 1
            left = left.left
        
        while right.right:
            right_depth += 1
            right = right.right