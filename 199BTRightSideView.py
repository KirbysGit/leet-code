# https://leetcode.com/problems/binary-tree-right-side-view
# medium

class firstAttempt:

    # 10 / 07 / 2025 - 10:08 pm

    # Runtime -> 0 ms - 100.00%
    # Memory - 17.71 MB - 60.81%

    # this is a new topic and i forgot how BFS worked so i used chatgpt to get
    # the general set up, because i knew i needed to use it, but once i saw how it
    # was set up i knew how to do it, just take per level the last node added to the
    # list and add that to a separate list then continue with the bfs. pretty simple.
    # but i didn't know how to use bfs so i cheated i guess.
    
    def bfs(self, currentLevel, rightSide):
        if not currentLevel:
            return

        totalLen = len(currentLevel)
        cur = currentLevel[totalLen - 1]
        rightSide.append(cur.val)

        nextLevel = []

        for node in currentLevel:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)

        self.bfs(nextLevel, rightSide)

    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightSide = []
        self.bfs([root], rightSide)

        return rightSide