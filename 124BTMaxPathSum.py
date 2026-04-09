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

class almostGotIt:

    # 04 / 08 / 2026 - 9:13 pm

    # test cases -> 54 / 96

    # alright so im pretty cloese to getting it, i probably could get it right now
    # but i think what i need is a bit of a refactor with the way im targeting the "max",
    # like where i'm at with the next easy change i would do i would have 5 nested max() 
    # statements, and i know thats not the best way to do it.

    # i just need to sit down and think about how the left and right nodes can be
    # combined, and compare with like how do we preserve if the root node is the highest or not.

    # i just want to think about it like that, like maybe passing the max value from the
    # initial left value over to the right to see if we can connect it that way.
    
    # because with every dp problem, you always just return the last value in the dp array.
    
    # and i know i can do that, im just figuring out how to.

    # my idea was really looking at a tree for a while and feeling like an inorder pathway
    # works the most. 

    # the main issue i was running into was that when i wanted to connect the paths,
    # i would end up taking the dp[-1] which could be the value of a different path,
    # but because its the highest value we've seen we take that, but those paths don't
    # connect that way, so i decided to use a dp for tracking max path values, and 
    # thne when i return the statements, we instead track the best value if we were
    # to continue the path upwards.

    # like return the highest value of the left and right paths combined with the root.

    # and now even reading that i feel like we can deal with the higher of left and right vs root
    # in that statement to save us the nested max() statements.

    # whatever tho, i'll deal with that when i come back to it, need to get some project time going.

    # here's the current code : 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root == None or (root.left == None and root.right == None):
            return root.val

        left_dp = []
        right_dp = []
        
        def recurse(root, dp):

            if root is None:
                return 0

            left = recurse(root.left, dp)

            print(dp)
            if not dp:
                dp.append(root.val)
            else:
                dp.append(root.val + dp[-1])
            
            right = recurse(root.right, dp)

            best = max(left, right)

            return root.val + best

        left = recurse(root.left, left_dp)
        right = recurse(root.right, right_dp)

        best = root.val + left + right
        left = max(left_dp) if left_dp else float('-inf')
        right = max(right_dp) if right_dp else float('-inf')


        return max(root.val, max(best, max(left, right)))