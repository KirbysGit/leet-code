# https://leetcode.com/problems/binary-search-tree-iterator/
# medium

class firstAttempt:

    # 04 / 12 / 2026 - 9:40 pm

    # Runtime -> 11 ms - 29.15%
    # Memory -> 25.61 MB - 38.49%

    # alright so apparently my solution is really slow, idon't really get why
    # because either way you do it you will need to touch every node which is what im doing?
    # but maybe you can track it with the next() function like just have next point to the next
    # recursive call of the function. idk honestly.

    # i was pretty lost on how i wanted to do this one until i looked at the topics.
    # my main issue was like i wanted to start at the start of the inorder and work my way over,
    # but  you need to start with the recursive call and preserve like the state of the previous
    # calls which is hard to do across functions. and thne i was like maybe we track a visited
    # array, which made more sense, but we'd have to deal with some bs with the visited as 
    # we could only start once we reached the left, adn it would have the same output.

    # then i saw the word "stack" in the topics and i was like fire!!! so i went ahead with that
    # basically just created a reverse inorder traversal inside of our _init_ and then created
    # a stack for them to add to, then if we call next we could just pop from the stack, and 
    # if we call hasNext we can just reference a boolean for if the stack has values or not!

    # here is my code : 

    def __init__(self, root: Optional[TreeNode]):

        def inorder(root):
            if root is None:
                return
            
            inorder(root.right)

            self.stack.append(root.val)

            inorder(root.left)

            return

        self.root = root
        self.stack = []

        inorder(root)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return bool(self.stack)