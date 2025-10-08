# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# medium

class firstAttempt:

    # 10 / 01 / 2025 - 3:59 pm

    # Runtime -> 131 ms - 85.59%
    # Memory - 32.00 MB - 87.20%

    # didn't have to use chatGPT!!!! did need to reference my old code but it was more 
    # just to see if i iterated recursively in the function. but anyways, my thought
    # after drawing out the tree was, okay initial base case with the none, the from
    # there how can we check if this node is greater than the prev node, and i was
    # like if we have the rootnode's val, and the prev node's val then we can check
    # based on that.

    # so i tried that but i only got 8 cases working, and i was looking at what cases
    # passed and i realized it was only comparing the previous value, but we need
    # to worry about the max value so far, so i adjusted prev val to max val and 
    # added a max update for if the value was bigger then we update it.

    # i used two functions again.

    # so check nodes, has the base case, an initial counter of zero, then a max check, 
    # if cur.val is greater than maxVal, we update it.
    # then if, cur.val is greater than rootVal and maxVal, we increment counter,
    # then recurse for left and right.

    # then in our main function we just make two calls to the checkNodes for the left
    # and right, then return and add 1 for the root "good" node.
    
    def checkNodes(self, cur: TreeNode, rootVal, maxVal) -> int:
        if not cur:
            return 0

        add = 0

        if cur.val >= maxVal:
            maxVal = cur.val

        if cur.val >= rootVal and cur.val >= maxVal:
            add +=1

        add += self.checkNodes(cur.left, rootVal, maxVal)
        add += self.checkNodes(cur.right, rootVal, maxVal)

        return add

        
    def goodNodes(self, root: TreeNode) -> int:
        leftGood = self.checkNodes(root.left, root.val, root.val)
        rightGood = self.checkNodes(root.right, root.val, root.val)

        return 1 + leftGood + rightGood