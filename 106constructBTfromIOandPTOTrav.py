# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# medium

class firstAttempt:
    
    # 04 / 01 / 2026 - 1:53 pm

    # Runtime -> 7 ms - 45.77%
    # Memory -> 21.10 MB - 68.44%

    # alright so i knew this was going to be similar to the previous problem
    # just because it shares the inorder, and i was guessing it would
    # just be an re-ordering of how we wrote hte solution, but looking at the way
    # post order is set up with the left -> right -> root then i realized it wouldn't
    # purely be a reordering but we need to handle how we pop differently too.

    # i was looking at the preivous question and i didn't realize one of the solutions
    # i was looking at was also discussing the postorder solution too
    # and i didn't really see anything except from the idea to pop solely fro mthe right.

    # originally in my preivous code thats what i was trying to do, i had set it up
    # with a swap boolean that basically updates every recursive call that swaps
    # the side of the array its popping from because in the inital test case thats how
    # the pattern connected, and it did work for the initial test case.

    # but after running i noticed that it wasn't working in general so i had to update
    # that and thats when i tried the pop from the right only and i noticed
    # that in the postorder array its basically the same except it builds from the right
    # so i revered the root.left and root.right recursive calls and then it works!

    # its still pretty slow, im guessing there is something else i am missing in 
    # terms of how we can optimize it, but i'll deal with that later when im
    # studying it more, something in here is reaching extra recursive calls that
    # are causing the slow down so theres def a better solution.

    # but here's mine ! 

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        mapping = {}

        for idx in range(len(inorder)):
            mapping[inorder[idx]] = idx

        postorder = collections.deque(postorder)

        def build(start, end):
            if start > end or len(postorder) == 0:
                return None

            root = TreeNode(postorder.pop())

            mid = mapping[root.val]

            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)

            return root

        return build(0, len(postorder) - 1)

class fasterSolution:

    # 04 / 01 / 2026 - 2:00 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 21.08 MB - 82.43%

    # alright so i was looking at the solutions tab, just trying to see the 
    # available solutions faster than the one i was using. and all they really did
    # was get rid of the use of the deque, becasue im guessing that adds an extra
    # operation, and thne with the pops from the deque as well, its a whole new O(N)
    # operation. 

    # instead these just used a more global index to keep track of where they were
    # in the postorder array, decrementing every time they created a new root, 
    # by doing this it made up for that bit of speed we were missing in the previous
    # attempt.

    # all i did was take out the deque, get rid of the pop, introduce the nonlocal index
    # and reference that for the new root.val from the postorder array.

    # here's the code : 

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        idx = len(postorder) - 1
        
        mapping = {}

        for idx in range(len(inorder)):
            mapping[inorder[idx]] = idx

        def build(start, end):
            nonlocal idx

            if start > end or len(postorder) == 0:
                return None

            root = TreeNode(postorder[idx])
            idx -= 1

            mid = mapping[root.val]

            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)

            return root

        return build(0, len(postorder) - 1)

