# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# medium

class firstAttempt:

    # 10 / 06 / 2025 - 3:39 pm

    # Runtime -> 53 ms - 63.82%
    # Memory - 22.29 MB - 20.54%

    # i ended up having to use chatgpt, but i think i had a right idea towards 
    # what i was trying to do. the goal was to basically find the node, then
    # just add the parents / ancestors to a list, then find the earliest
    # common ancestor from said list and return that.

   # so i keep a found falg because i hate recursion passing values.

   # then i have the ancestorsList function which is just a dfs that adds the ancestors
   # after the value is found.
   
   # then we have the main function which calls the ancestorsList function to get the
   # ancestors for both p and q, then we iterate through the lists and find the earliest
   # common ancestor. 

   # i really got to get some more practice in with recursion and passing value bc
   # i am dookie at them right now, but i am . getting better . 

   # definitely a simpler way to do this, but it works right now so. 
    def __init__(self):
        self.found = False

    def ancestorsList(self, desired, parent, cur, ancestors):
        if cur == None:
            return

        if cur.val == desired.val:
            self.found = True
        
        if self.found == True:
            ancestors.append(cur)
            return
        else:
            self.ancestorsList(desired, cur, cur.left, ancestors)
            if self.found:
                ancestors.append(cur)
                return
            
            self.ancestorsList(desired, cur, cur.right, ancestors)
            if self.found:
                ancestors.append(cur)
                return
        
        return

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root

        pAncestors = []
        qAncestors = []

        self.found = False
        self.ancestorsList(p, root, root, pAncestors)

        self.found = False
        self.ancestorsList(q, root, root, qAncestors)

        for node in pAncestors:
            if node in qAncestors:
                return node

        return root

class fuckYou:

    # i just saw this and got mad. bro 5 lines.

    # i need to be able to turn my complexx approaches into simple applications bruh.

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        return root if l and r else (l or r)

class backFor150Interview:

    # 04 / 16 / 2026 - 3:34 pm

    # Runtime -> 51 ms - 92.91%
    # Memory -> 24.39 MB - 81.32%

    # i was pretty unsure of what to do, i was thinking like how to properly track the ancestors.
    # but then as i was walking my way through some of the trees recursively, i realized that
    # if you don't get a value on the left and right, then you just take the first value you
    # see on whichever side comes back, becasue it is the latest ancestor we will have seen,
    # there's no reason to verify the child is below it as we already know that if we couldn't
    # find it on the other side we were looking.

    # this allows us to to just retrun the root if we find p or q, and if we find both
    # we can return the parent of what was returned from left and right which would be the root.

    # here's the code (basically the same as the fuckYou class just a bit longer) : 

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)        

        if L and R:
            return root
        elif L:
            return L
        elif R:
            return R
    
