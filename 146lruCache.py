# https://leetcode.com/problems/lru-cache/description/
# medium

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class firstAttempt:

    # 03 / 06 / 2026 - 3:24 pm 

    # still in process. thinking

    # initialize just sets up the general structure we need.
    # get, fetches value from dict, updates order of the list.
    # put, adds value to dict, updates order of list, assuming less than capacity.

    class LRUCache:

    def __init__(self, capacity: int):
        self.track = {}
        self.max = capacity
        self.space = 0
        self.front = ListNode(0, None)
        self.cur = self.front

    def get(self, key: int) -> int:
        if key in self.track:
            
            return self.track.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.space != self.max:
            self.track.update({ key : value })
            self.cur.val = key
            new = ListNode(0, None)
            self.cur.next = new
            self.cur = self.cur.next
            self.space += 1
        else:
            self.track.pop(self.front.val)
            self.front = self.front.next
            new = ListNode(key, None)
            self.cur.next = new
            self.cur = self.cur.next

        print(self.track)
        print(self.front)


class secondAttempt:

    #  03 / 08 / 2026 - 4:27 pm

    # bro this problem is like still fucking me up. its really just like i want to use a stack, but you can't pop off the
    # bottom of a stack. i think i need to draw it out completely then come back to it.

    # its really just like small things i don't think about. my approach is right, but i need to clean up the implementation.

    class LRUCache:

    def __init__(self, capacity: int):
        self.track = {}
        self.stack = ListNode(0)
        self.cur = self.stack
        self.nodes = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        if self.track.get(key):
            val = self.track.get(key)
            self.cur.next = ListNode(key)
            self.cur = self.cur.next
            if self.nodes == self.cap:
                self.stack = self.stack.next
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check if cur space == capacity.
            # if so, 
                # get rid of LRU.
                # add cur key and val to end.
            # if less,
                # add cur key and val to end.
        if self.nodes == self.cap:
            # add new node.
            new = ListNode(key)
            self.cur.next = new
            self.cur = self.cur.next
            self.track.setdefault(key, value)

            # remove front node.
            remove = self.stack.val
            self.track.pop(remove)
            self.stack = self.stack.next
        else:
            # add new node.
            new = ListNode(key)
            self.cur.next = new
            self.cur = self.cur.next
            self.track.setdefault(key, value)
            
        print(self.stack.next.val)
        print(self.cur.val)