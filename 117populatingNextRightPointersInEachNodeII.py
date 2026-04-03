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
        
class imTheGoat:

    # 04 / 03 / 2026 - 2:41 pm

    # Runtime -> 44 ms - 91.67%
    # Memory -> 20.43 MB - 45.55%

    # i was coming back, literally saying to myself like, lets not get married to this approach
    # trying to just use a singular bfs to track the next node as we cant tell the split.
    
    # i tried to figure out patterns, i drew out BFS right and left at same time to see if
    # we could connect them, but iterations got weird so i didn't go too far into that one.

    # then i drew out the preorder, inorder, and postorder to see if there is a way to connect
    # those values but it didn't really seem like one.

    # so i came back to the bfs and was planning out how to split the rows based on whats 
    # picked up per queue run, and i had the hidea to split it into multiple while loops
    # to handle the different rows. 

    # like two sorts of queues, one for this current level's node, then one for then next level's nodes.

    # so the BFS queue would expand as it moves downwards and connect across in the way the nodes
    # are seen in a BFS.
    
    # i implemneted that, then it worked!!

    # here is the code : 

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        toVisit = collections.deque([root])
        curVisit = collections.deque([])

        while toVisit:
            curVisit = toVisit
            toVisit = collections.deque([])
            while curVisit:
                top = curVisit.popleft()

                if curVisit:
                    top.next = curVisit[0]
                else:
                    top.next = None
                
                if top.left:
                    toVisit.append(top.left)
                if top.right:
                    toVisit.append(top.right)
        
        return root