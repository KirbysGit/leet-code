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

    # Runtime -> 0 ms - 100.00%
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

class fasterSolution:

    # 04 / 15 / 2026 - 10:44 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 23.74 MB - 57.87%

    # alright i don't think i would've gotten this.

    # i mean it makes sense in hindsight but really its just like a weird recursion.

    # like the heights make sense, but the idea of the recursion still going through each
    # node in a non-even tree is where i was kind of thrown off, like i felt like that 
    # was too slow.

    # i was just overthinking it seeing it had to be faster than O(n), so i wanted to find
    # an algorithm that was like O(log n) or something.

    # the idea behind the code is to recursively check the left and right heights, 
    # then compare, and if they're not the same, then we know the tree is not complete, so we
    # recurse the function to check the heights of the left and right subtree, and eventually
    # it will find "perfect" subtrees and return their number without parsing through each node
    # but the tree that isn't perfect will have to keep recursing down until it finds 
    # the tree that is imperfect.

    # looks pretty simple after typing it out but its pretty hard to think about recursing
    # like that. but it makes sense.

    # here's the code :

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = get_left_height(root.left)
        right_height = get_right_height(root.right)

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def get_right_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height