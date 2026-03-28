# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# medium

class breakingItDown:

    # 03 / 28 / 2026 - 4:37 pm

    # alright so this question is fucking with me. i can't really connect any dots in my head yet.

    # at first i thought it was easy, but the idea of how its set up creates like issues with
    # knowing whether the children are left or right.

    # from what i've understood about the traversals :
    # - PREORDER -> regular DFS traversal
    # - INORDER -> DFS but going down the entire left subtree before the right.

    # so with our example it leaves us with :

    # preorder = [3, 9, 20, 15, 7]
    # inorder  = [9, 3, 15, 20, 7]

    # also understanding this test case is very limited is important too, like i can't really do
    # much if i just base my reasoning on this, i need to consider more children.

    # right now i know these :

    root.val = preorder[0]
    head = root.val

    if inorder[0] != root.val:
        for val in inorder:
            if val == root.val:
                # swap to the right tree from root.
            else:
                # move down the tree.
                # meat of the problem.
                # i don't get how we can use both arrays at one time to find the true output.

    # i'll be working on this for a bit i can tell. but i'll get it!