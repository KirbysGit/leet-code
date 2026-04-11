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


class symptomHandling:

    # 04 / 09 / 2026 - 2:30 pm

    # test cases -> 79 / 96

    # i'm really just symptom handling right now.

    # i'm gonna head to the gym but leave this open so i can think about it more when i get back.
    
    # its really just gotta be a way i organize the conditionals so we add only when the 
    # value is higher than the previous value.

    # here's current code, (its getting long bro):

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root == None or (root.left == None and root.right == None):
            return root.val

        left_dp = []
        right_dp = []
        left = 0
        right = 0

        def recurse(root, dp):

            if root is None:
                return 0

            left = recurse(root.left, dp)

            if not dp:
                dp.append(root.val)
            else:
                cur = root.val + dp[-1]
                if root.val > cur:
                    dp.append(root.val)
                else:
                    dp.append(cur)
            
            right = recurse(root.right, dp)

            best = max(left, right)

            up = root.val + best

            return max(root.val, up)

        if root.left:
            left = recurse(root.left, left_dp)

        if root.right:
            right = recurse(root.right, right_dp)

        solutions = []
        
        solutions.append(root.val + left + right)
        solutions.append(root.val + left)
        solutions.append(root.val + right)
        solutions.append(root.val) 
        if left_dp:
            print(left_dp)
            solutions.append(max(left_dp))
        if right_dp:
            print(right_dp)
            solutions.append(max(right_dp))
        
        print(solutions)

        return max(solutions)

class idekSlowASFTho:

    # 04 / 11 / 2026 - 12:10 am

    # Runtime -> 22 ms - 6.08%
    # Memory -> 24.06 MB - 19.29%

    # alright bro this shit took me a minute, i've been working on it probably since like 10 ish?

    # but i was pacing around the kitchen trying to understand wtf this was asking for, so 

    # like dude, theres so many cases, like you have to handle the sub-paths, and the potential single node
    # paths, and then connecting over.
    
    # my main idea was trying to like lets track the current path as we go through, add them at the end of a path
    # so when we reach a leaf node, and then add that path to the dp if its greater than the current last max value.

    # but it feels pretty slow, i actualy realized i had a print statement in the middel of the code and i realized
    # i can just do if statements to add to the dp instead of a max() statement at the end.

    # so i re-did runtime and now its : 

    # Runtime -> 8 ms - 60.85%


    # i'll go through faster shit tmrw, but for now here's the code :

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root is None or (root.left is None and root.right is None):
            return root.val
    
        dp = [root.val]

        def recurse(root, dp, path):

            if root.left is None and root.right is None:
                return root.val

            path = root.val

            right = None
            left = None

            if root.left:
                left = recurse(root.left, dp, path)
                if left > dp[-1]:
                    dp.append(left)

                if root.val + left > root.val:
                    path += left

            if root.right:
                right = recurse(root.right, dp, path)
                if right > dp[-1]:
                    dp.append(right)

                if root.val + right > root.val:
                    path += right

            if path > dp[-1]:
                dp.append(path)

            if right != None and left != None:
                sub = max(right, left)
            elif right != None:
                sub = right
            elif left != None:
                sub = left

            return max(root.val, root.val + sub)

        recurse(root, dp, 0)

        return dp[-1]
            

class fasterSolution:

    # 04 / 11 / 2026 - 4:29 pm

    # Runtime -> 5 ms - 84.70%
    # Memory -> 23.85 MB - 70.90%

    # i got this one off the solutions tab and decided to review it with chatgpt.

    # this honestly was the idea i was going for, but i couldn't figure out how to deal with handling two
    # different values at once, like returning the best path up, and the best value up, like those are two
    # different things. 

    # when reviewing with mrgpt it brought up how the problem has two separate quantities ;
    # - what can i return to my parent?
    # - what is the best path seen anywhere so far? 

    # this is what i was asking, but i was struggling to find a way to combine it per run.

    # the clean solution keeps track of the best value with the nonlocal variable with res. 

    # then it recurses left and right, ignoring negative branches, which is another idea i was trying
    # to implement, as its better to stop than include a harmful path.

    # update our dp max through a max statment between current best and current path.

    # and we only want to return one side up, so at each like path, we're checking the path
    # max then moving up and returning just one side of the path of the parent so it can
    # recompute based on its two children.

    # hate to sound like an idiot but i had the idea, implementation wasn't there tho. 

    # here's the code : 

    res = root.val

    def dfs(root):
        if not root:
            return 0

        nonlocal res

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        res = max(res, root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res