# https://leetcode.com/problems/lru-cache/description/
# medium

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


               
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next