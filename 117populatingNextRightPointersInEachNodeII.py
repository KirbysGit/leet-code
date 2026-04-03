# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
# medium

class tryingToPlan:

    # 04 / 02 / 2026 - 10:41 pm

    # this problem is actually pretty tough, like i really and just missing how i can connect.

    # in reality if i could just draw it out, its pretty simple, i just need to connect whatevers
    # left to right per row, but figuring out the "per row", is where im struggling.

    # the idea for me right now is to us a bfs to go through the tree, and connect the nodes per row.

    # but the problem is that with each queue addition, it doesn't really preserve what was on that row? 
    
    # and we can't do indexes because there are cases where the tree is not even in any way, so 
    # im trying to think of a way to go through each row using bfs and split it so we connect
    # in a direct way through each row, from node to node, and then the last node to nothing.

    # all i have is a BFS set up but heres what i have so far : 

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        queue = collections.deque([root])

        visited = set()

        while queue:
            top = queue.popleft()
            visited.add(top)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        