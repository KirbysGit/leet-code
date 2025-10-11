# https://leetcode.com/problems/delete-node-in-a-bst/
# medium

class firstAttempt:

    # 10 / 11 / 2025 - 2:48 am

    # Runtime -> 0 ms - 100.00%
    # Memory -> 21.29 MB - 94.52%

    # i had to use chatgpt :(
    
    # alright i went through multiple phases with this shit over the last couple hours

    # first off i was like let me adjust BST to just get the node, but them im like okay i need the parent value
    # to actually "delete" it, but adjusting the reference from the parent

    # then i set it up to return the parent node with the BST, but then i was like okay how do i update with
    # all of these cases

    # then i realized i didn't need the parent, i could just update the values directly with some series of 
    # if statements

    # then i was like okay that works but it doesn't work with if the case that the val is the root
    # and i was trying to set it up for that, but the proper rotation was super tricky for me, and thats
    # when i reached to mrGPT for some aid, and i realized i could kind of do it all in one function.

    # the solution is set up a binary search in teh main function where if we get the value, 
    # check if left child, if not return right,
    # check if right child, if not return left,
    # then if has both children, find smallest value in right subtree,
    # then replace root with that value and delete node with smallest value in subtree
    # kind of seems like a lot but its just a BST with a case to find smallest value and replace it

    def findMin(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)

        return root