# https://leetcode.com/problems/leaf-similar-trees/
# easy

class firstAttempt:

    # 09 / 30 / 2025 - 5:56 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 18.02 MB - 5.13%

    # had to use gpt but i got close with some hints from it.

    # still so weird to think about the process of it, because i was trying to think
    # about it like maxdepth per tree, but i wasn't thinking about using a separate function
    # so it really wasn't making any sense to me. 

    # eventually chatgpt mentioned using another function which made it much simpler
    # in my brain, but still i was like okay we just need to add the leaf to a list
    # then return back up, and then compare? but it feels slow, like i feel like 
    # there is a way to do it without using a separate function but i'd really have
    # to break down the process and think about it more.

    # but what our solution does is utilize collectLeaves which basically is that
    # same sort of recursive call, except if the node doesn't have any children, aka
    # a leaf, we add it to the list. then recurse the left and right children.

    # then from there we just use that function on the two trees, and compare the lists.

    def collectLeaves(self, node: Optional[TreeNode], leaves_list):
        if not node:
            return
        if not node.left and not node.right:
            leaves_list.append(node.val)
            return

        self.collectLeaves(node.left, leaves_list)
        self.collectLeaves(node.right, leaves_list)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        tree1 = []
        tree2 = []

        self.collectLeaves(root1, tree1)
        self.collectLeaves(root2, tree2)

        if (tree1 == tree2):
            return True
        
        return False