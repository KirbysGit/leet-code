# https://leetcode.com/problems/copy-list-with-random-pointer/
# medium

class firstAttempt:

    # 02 / 16 / 2026 - 4:33 pm

    # bro i've been so fucking exhausted this morning i literally used
    # chatgpt to solve the problem and i still don't even know how to do it.

    # im coming back to this problem tmrw and i'll solve it on my own, i have
    # no recollection of what chatgpt told me so it will basically be 
    # starting out fresh!!

    # still super fucking tired right now so imma just pause.

    # idea was like two pass, one for list and one for random pointers.

    # in my initial attempt i was trying to understand how to use
    # a hashmap to store the nodes so i could reference them properly.

class correct:

    # 02 / 17 / 2026 - 9:06 pm

    # Runtime -> 45 ms - 58.58%
    # Memory -> 20.10 MB - 43.79%

    # i'm still kind of lost with this. linkedlists are so fucking confusing to me.

    # basically its like we copy everything over with a hashmap, but we do it in two passes.

    # im just lost on the connections between.
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        mapping = {}

        cur = head
        while cur is not None:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur is not None:
            mapping[cur].next = mapping.get(cur.next)
            mapping[cur].random = mapping.get(cur.random)

            cur = cur.next

        return mapping[head]
        