# https://leetcode.com/problems/symmetric-tree/
# easy

class firstAttempt:

    # 03 / 25 / 2026 - 9:30 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.54 MB - 13.42%

    # alright this was pretty hard for me honestly.

    # like teh code was one thing, but the connection in my brain on how to 
    # create the algorithm was not clicking.

    # i didn't use any outside help other than searching up how to create
    # the bfs algorithm because i was thinking about how it moves through
    # the tree because i was using a visualizer, because i remembered how
    # it moved, but it was way different when it comes to how you
    # want to set it up to move. 

    # but i think this problem would work with DFS too, at least with the 
    # way i set it up.

    # i was really struggling trying to connect how we can have two recursive
    # calls to the same function going at the same time, comparing nodes
    # on different sides of the tree, that really didn't make much sense to me.

    # what i did though was pretty complicated honestly, im sure there is a 
    # much simpler answer that i will see tonight or tmrw. 

    # my approach was to use two bfs functions, one that goes to the left
    # first and one that goes to the right first. each of these bfs
    # functions will return a list of the the vals in the order it saw them
    # and then compare the two lists to see if they are the same.

    # i had to add some extra checks to handle the edge cases with the "None"
    # values because i needed to add specific values instead so i did that.

    # here is the code : 

    def __init__(self):
        self.left = []
        self.right = []

    def bfsLeft(self, root):
        
        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            self.left.append(node.val)
            if node.left:
                queue.append(node.left)
            else:
                self.left.append(0)
            if node.right:
                queue.append(node.right)
            else:
                self.left.append(1)
    
    def bfsRight(self, root):

        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            self.right.append(node.val)
            if node.right:
                queue.append(node.right)
            else:
                self.right.append(0)
            if node.left:
                queue.append(node.left)
            else:
                self.right.append(1)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        self.left = []
        self.right = []
        
        self.bfsLeft(root.left)

        self.bfsRight(root.right)

        return self.left == self.right


class someGeniusShit:

    # 03 / 25 / 2026 - 9:43 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.54 MB - 13.42%

    # i saw this in the suggest solutions tabs.

    # this shit is so smart, this is what my brain was trying to connect to
    # i didn't even think about passing the nodes like this.

    # i was trying to do like dfs(left) dfs(right) but comparing the nodes
    # at hte same time and just connecting the nodes like that is way smarter.

    # also, i was really struggling mentally clicking the base case, like how do
    # the left and the right nodes qualify for the base case? like if they're
    # none? and then when i see this it appears super obvious to do the
    # AND vs OR comparison.

    # its a pretty basic recursion. here it is : 

    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.right, root.left)

    # bro i typed that without looking at the screen. im goated.