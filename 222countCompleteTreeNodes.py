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

class oNSolution:
    
    # 04 / 14 / 2026 - 2:26 pm

    # Runtime -> 3 ms - 45.63%
    # Memory -> 23.77 MB - 58.87%
    
    # looking at the discussion most of the solutions were just supposed to be O(n).

    # the extra ask was making it faster than that, so i just did O(n) here and going to
    # come back to see if i can get faster than O(n) later.

    # i mean i get how to do it conceptually, its just like how do you binary search
    # without approach O(n) anyways?

    # here's my O(n) code : 

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root):
            nonlocal total
            total += 1
            if not root.left and not root.right:
                return

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

            return


        total = 0

        dfs(root)

        return total