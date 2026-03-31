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

class startingTheCode:

    # 03 / 29 / 2026 - 9:47 pm

    # alright so my brain hurts, or just feels bad right now, its because its growing!!

    # nah i mean its hard connecting all of these dots right now, i was drawing out
    # some examples of the trees trying to understand how they connect, and how we
    # can handle adding the nodes to the proper spots. 

    # i think i need to experiment with some larger test cases, but right now
    # im really just trying to connect the pattern i see from the way
    # the arrays interact.

    # here is my current code :

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # iterating through both at same time.

        # root = preorder[0]
        # add values to added = [] every run

        # thinking to have a toggle, for left or right toggle.
        
        # start out left. swap at root node in inorder.

        def addNode(direction, head, value):
            new = TreeNode(value)
            if direction:
                head.left = new
            else:
                head.right = new
                

        root = TreeNode(preorder[0])

        head = root

        idx = 0

        added = set(preorder[0])

        direction = True # True -> Left

        while idx < len(preorder):
            if inorder[idx] == root.val:
                direction = !(direction)
                continue
            elif preorder[idx] in added and inorder[idx] in added:
                # increment and continue on, nothing to do.
                idx += 1
                continue
            elif preorder[idx] in added:
                # if just preorder in, add 
                self.addNode(direction, head, inorder[idx])
                #direction = !(direction)
            elif inorder[idx] in added:
                # add node with opposite direction of current
            else:
                if inorder[idx] == preorder[idx]:
                    new = TreeNode(preorder[idx])
                    if direction:
                        tmp = root.left
                        root.left = TreeNode(preorder[idx])
                        root.left.left = new
                    else:
                        tmp = root.right
                        root.right = TreeNode(preorder[idx])
                        root.right.right = new
                else:
                    # add the child based on direction?


        # direction seems to be the biggest thing messing with me, but i feel like i have
        # to do it that way, its just weird in my head about like how can we deal
        # with the direction like which child we place, based on whats available. 

        # also like proper either "adding" or like "stacking" of the nodes is a struggle, like
        # when should we do each one ? 

        # i'll be back bro.

class hintAndIGotIt:

    # 03 / 30 / 2026 - 10:56 pm

    # Runtime -> 134 ms - 8.67%
    # Memory -> 55.84 MB - 41.51%

    # alright so its really slow but it works. which is important to me. 

    # basically, i was working through all of the patterns with me trying to understand how
    # we can iterate through both the arrays at the same time and connect how they
    # are added on top of each other, like how can we use the direction variable and alter
    # it properly to handle adding the nodes in the proper order.

    # but i spent like probably 6 hours or so over the last days trying to understand it
    # but yea nothing made sense, there was always just a break case later in the test case.

    # i caved man. i used chatgpt. NO!!!!! nah but i mean, i just asked for a hint and this is
    # what it gave me or at least the part i let myself read : 

    # preorder tells you who the root is next, inorder tells you where that root splits left subtree from right subtree.

    # right after it said my approach was "yea, you're pretty far off with the directions idea"

    # gotta love the brutal honestly ig. but as soon as i saw that, it STILL didn't click.

    # i drew out some examples on the whiteboard, and the pattern i noticed made sense but i 
    # realized i needed to recurse which isn't my favorite.

    # but basically the idea is what chatgpt gave me, with the, use the next preorder value as your
    # root, and pass the inorder splits to the recursed case with the next root.

    # i think the reason mine is so slow is because of the way i iterate through, there is definitely a 
    # more efficient way to do it but i'll deal with that tmrw because i've been working on this for like 2
    # hours straight now no breaks.

    # here is my code :

    # idea is to recursively split and pass new root downwards until the values are None, then 
    # make way back up. to better handle the proper root without like a global val i used 
    # a deque i pass through. 

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def split_arr(root, in_arr):
            idx = 0
            while in_arr[idx] != root:
                idx += 1

            if idx == 0 and len(in_arr) > 0:
                return None, in_arr[1:]
            elif idx == 0:
                return None, None

            left = in_arr[:idx]
            right = in_arr[idx + 1:]

            return left, right

        
        def recurse(preorder, side):
            if not preorder:
                return None

            root = TreeNode()
            root.val = preorder.popleft()

            left, right = split_arr(root.val, side)

            if not left and not right:
                return root
            if left:
                root.left = recurse(preorder, left)
            if right:
                root.right = recurse(preorder, right)

            return root

        pre = 0
        pre_dq = deque(preorder)
        root = TreeNode(pre_dq.popleft())

        left, right = split_arr(root.val, inorder)
        
        root.left = recurse(pre_dq, left) if left else None
        root.right = recurse(pre_dq, right) if right else None

        return root


