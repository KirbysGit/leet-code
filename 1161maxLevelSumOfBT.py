# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
# medium

class firstAttempt:

    # 10 / 08 / 2025 - 3:38 pm

    # Runtime -> 4 ms - 99.42%
    # Memory -> 21.74 MB - 44.72%

    # no chat gpt!!

    # i mean idk if this is a dumb thought, but looking at some of these problems once you have the 
    # approach you need to take, like DFS, BFS, its just customizing a couple of lines.

    # like outside of the regular BFS all we do is pass levelIdx and maxLevel and maxSum, 
    # then update the maxLevel based on some of the other data, like we could remove like 4
    # lines and it be a normal BFS. 

    # but yea man simple approach BFS, get curSum for this curLevel then check if bigger
    # than maxSum, if so update maxSum and maxLevel then continue with BFS.

    def bfs(self, levelNodes, maxSum, levelIdx, maxLevel):
        if not levelNodes:
            return maxLevel

        nextLevel = []
        curSum = 0

        for node in levelNodes:
            curSum += node.val
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)

        if curSum > maxSum:
            maxSum = curSum
            maxLevel = levelIdx

        return self.bfs(nextLevel, maxSum, levelIdx + 1, maxLevel)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:        
        return self.bfs([root], float('-inf'), 1, 1)