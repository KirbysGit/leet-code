# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# hard

class planningItOut:

    # 04 / 07 / 2026 - 2:26 pm

    # alright so this one is definitely a hard problem, but i know i can get it
    # i just need to get the path to click, like the hardest part right now
    # is making sure that the tree while iterating through stays in a path, 
    # like moving across the tree if needed. 

    # like looking at the 2nd example, its like :

    #               -10
    #             /      \
    #          9          20
    #                   /    \
    #                 15       7

    # the max path sum is 42, which is 15 -> 20 -> 7,
    # so when considering the path, we need to do like some sort of dfs
    # tracking the highest value as we go, but the starting point is important
    # as we iterate, we need to consider each branch and see what the highest value
    # is at that point.

    # like the problem is with my simple like coded in 2 second approach right now
    # is that it works off the last value of the dp, which means it doesn't consider
    # the path, like look at this output :

    # []
    # [-10]
    # [-10, 9]
    # [-10, 9, 29]
    # [-10, 9, 29, 44]

    # if we can get it to work just off of the value we know is connected then
    # we can get the max path sum.

    # here's my current code :

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        dp = []
        
        def recurse(root, dp):

            if root == None:
                return

            print(dp)
            if not dp:
                dp.append(root.val)
            else:
                cur = root.val + dp[-1]
                if cur < root.val:
                    dp.append(root.val)
                elif cur > dp[-1]:
                    dp.append(cur)
                else:
                    dp.append(dp[-1])

            recurse(root.left, dp)
            recurse(root.right, dp)

            return

        recurse(root, dp)

        return max(dp)
