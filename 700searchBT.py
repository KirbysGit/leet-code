# https://leetcode.com/problems/search-in-a-binary-search-tree/
# easy

class firstAttempt:

    # 10 / 09 / 2025 - 4:14 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.09 MB - 91.49%

    # no chatgpt! IM GOATED!!

    # i mean it was a pretty easy problem, but i overcomplicated it for a second.
    # i had to draw it out because i was so confused on how we were going to
    # traverse the tree to get the subtree after we found the node, because 
    # it looked like it was in array format, but the output was actually just figuring
    # out the subtree so all we had to do was return the cur node and it formats
    # as the subtree itself.

    #  but pretty simple, if val is cur node, return that,
    #  else, if less than, go left, if greater than, go right, then return that value.

    # i had the val set to arr because i thought it was an arr. 

    def move(self, cur, val):
        if cur is None:
            return None

        if cur.val == val:
            return cur
        elif cur.val > val:
            arr = self.move(cur.left, val)
        else:
            arr = self.move(cur.right, val)
        
        return arr
        
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.move(root, val)