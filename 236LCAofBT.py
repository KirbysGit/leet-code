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