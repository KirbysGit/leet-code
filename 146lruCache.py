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


class thirdAttempt:

    # 03 / 19 / 2026 - 1:50 pm

    # testcases -> 7 / 24 passed.

    # and we're back! 

    # highkey been avoiding this problem because its just so hard, but i literally figured out my main
    # issue really quick, then i've been dealing with a couple of new ones now that are harder to deal with.

    # coming back one of the main issues was that i wasn't even incrementing the nodes, so like we would
    # just add and add, and then get rid of based on the "stack" i created, so a couple of fixes helped that out.

    # then i ran into an issue with the key value being 0 which wouldn't pass the if statement, so i just
    # had to handle that with a -1 and setting up the conditional statement differently.

    # and then now where i am is that when you add a new node that has the same key, so my brain is thinking
    # like its pretty easy to handle in some cases, but in set ups where the node isn't the last one used,
    # then we have to iterate through the list to find the node and then move it to the front. updating
    # the value in the dict is easy, thats just another statement, but i feel like there is a better way
    # to move the node to the front and ignoring the past node without having to iterate through the list.

    def __init__(self, capacity: int):
        self.track = {}
        self.stack = ListNode(-1)                    # original ptr.
        self.cur = self.stack                       # cur is moving ptr.
        self.nodes = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.track:                     # if key exists in track dict.
            val = self.track.get(key)               # get val at key.
            self.cur.next = ListNode(key)           # move value forward to node we just used.
            self.cur = self.cur.next                # move cur to that new value.
            if self.nodes == self.cap:              # if we're at cap, move stack forward.
                self.stack = self.stack.next
            return val                              # return val we got.
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.track:
            self.track.setdefault(key, value)

        if self.nodes == self.cap:                  # if at capacity.
            new = ListNode(key)                     # create new node.
            prev = new
            self.cur.next = new                     # update cur ptr to new node.
            self.cur = self.cur.next                # move cur forward.
            self.cur.prev = prev
            self.track.setdefault(key, value)       # place new key in dict.

            remove = self.stack.val                 # grab val to remove.
            self.track.pop(remove)                  # remove from dict.
            self.stack = self.stack.next            # move stack ptr forward.
        else:
            if self.stack.val == -1:
                self.stack.val = key
            else:
                new = ListNode(key)
                prev = new
                self.cur.next = new
                self.cur = self.cur.next
                self.cur.prev = prev

            self.track.setdefault(key, value)
            self.nodes += 1

class fourthAttempt:

    # bro i gotta hit a reset on this one its killing me.

    # 03 / 20 / 2026 - 2:38 pm

    # testcases -> 15 / 24 passed.

    # alright so we made progress, a bit backwards and a bit forwards but i'm getting closer.

    # its really handling like the None's that really mess me up.

    # basically i ran into some cases where the stack was being rearranged poorly when we
    # had a value that already existed in the stack, so like the way i handle moving the
    # values around was really causing issues. 

    # i resolved some of them, but now im getting an issue with a larger test case, and its
    # harder to just draw out. i think i need to approach the entire problem again, like
    # drawing out what the entire cases could be, just so i can avoid what i am doing right
    # now with all of the symptom handling i've been doing. 

    # here is the current code : 

    def __init__(self, capacity: int):
        self.track = {}
        self.stack = ListNode(-1)                    # original ptr.
        self.cur = self.stack                       # cur is moving ptr.
        self.nodes = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.track:                     # if key exists in track dict.
            val = self.track.get(key)               # get val at key.
            self.cur.next = ListNode(key)           # move value forward to node we just used.
            self.cur = self.cur.next                # move cur to that new value.
            if self.nodes == self.cap:              # if we're at cap, move stack forward.
                self.stack = self.stack.next
            return val                              # return val we got.
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # checking if the key is already in our list, then updating the dict value
        # and connecting the node to the front. 
        if key in self.track:
            self.track[key] = value
            if self.stack.val != key:
                front = self.stack
                while front.val != key:
                    front = front.next
                front.prev.next = front.next
                if front.prev.next == None:
                    self.cur = front.prev
                else:
                    self.cur = front.prev.next
            else:
                if self.stack.next:
                    self.stack = self.stack.next

            new = ListNode(key)
            prev = self.cur
            self.cur.next = new
            self.cur = self.cur.next
            self.cur.prev = prev

            return


        if self.nodes == self.cap:                  # if at capacity.
            new = ListNode(key)                     # create new node.
            prev = self.cur
            self.cur.next = new                     # update cur ptr to new node.
            self.cur = self.cur.next                # move cur forward.
            self.cur.prev = prev
            self.track.setdefault(key, value)       # place new key in dict.

            remove = self.stack.val                 # grab val to remove.
            self.track.pop(remove)                  # remove from dict.
            self.stack = self.stack.next            # move stack ptr forward.
        else:
            if self.stack.val == -1:
                self.stack.val = key
            else:
                new = ListNode(key)
                prev = self.cur
                self.cur.next = new
                self.cur = self.cur.next
                self.cur.prev = prev

            print(self.stack.val)
            print(self.stack.next)
            self.track.setdefault(key, value)
            self.nodes += 1

class fifthAttempt:

    # 03 / 22 / 2026 - 3:49 pm

    # holy fuck.

    # Runtime -> 4780 ms - 5.01%
    # Memory -> 78.52 MB - 27.53%

    # dude this question was so ass its insane. literally cursing out my computer like 10 minutes ago.

    # just so many dumb things to handle while moving the nodes around. like in reality the problem isn't
    # hard to conceptualize, but just using the data structures i did, to handle the problem was so fucking ass.

    # took me so long, i mean i was working on this problem before my michigan trip so its been like 2 weeks
    # with this problem mentally in my background.

    # look at this stat bro from leetcode : Time taken: 14d 14hrs 48m 51s

    # insane.

    # anyways, i don't really know how to explain what i did, i just got the code to work to how i was 
    # thinking about it.

    def __init__(self, capacity: int):
        self.track = {}                 # dict for tracking vals in LRU.
        self.LRU = ListNode(-1)         # node @ this point is the LRU.
        self.cur = self.LRU             # node @ this point is the MRU.
        self.nodes = 0                  # number of nodes we have in LRU.
        self.cap = capacity             # capacity of nodes for this LRU.

    def get(self, key: int) -> int:
        if key in self.track:
            val = self.track.get(key)

            front = self.LRU
            if self.cur.val == key:
                return val
            if front.val == key:
                if self.LRU.next != None:
                    self.LRU = self.LRU.next
                else:
                    return val
            else:           
                front = self.LRU
                while front.val != key:
                    prev = front
                    front = front.next

                prev.next = front.next

            new = ListNode(key)             # create new node, and add to front.
            self.cur.next = new
            self.cur = self.cur.next
            front = self.LRU
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.track:
            self.track[key] = value
            front = self.LRU
            if self.cur.val == key:
                return

            if front.val == key:
                if self.LRU.next != None:
                    self.LRU = self.LRU.next
                else:
                    return
            else:

                while front.val != key:
                    prev = front
                    front = front.next

                prev.next = front.next

            new = ListNode(key)             # create new node, and add to front.
            self.cur.next = new
            self.cur = self.cur.next
        else:
            if self.nodes == self.cap:
                remove = self.LRU.val           # grab key to remove from dict based on LRU.
                self.track.pop(remove)          # remove from dict.

                new = ListNode(key)             # create new node, and add to front.
                self.cur.next = new
                self.cur = self.cur.next

                self.LRU = self.LRU.next        # get rid of LRU.

                
                self.track.setdefault(key, value)
            else:
                self.track.setdefault(key, value)
                self.nodes += 1

                if self.cur.val == -1:          # if first node, just update value.
                    self.cur.val = key
                else:                           # else, create new node, and add to front.
                    new = ListNode(key)
                    self.cur.next = new
                    self.cur = self.cur.next

        front = self.LRU

class fasterWay:

    # 03 / 23 / 2026 - 8:42 pm

    # i left off this problem yesterday with a very slow solution, and reviewing some more proper
    # solutions, i found some with OrdereredDict to be the fastest, and some with a normal
    # Doubly Linked List, which is what I originally attempted, but I don't really use in my approach.

    # Runtime -> 124 ms - 55.87%
    # Memory -> 78.89 MB - 11.10%

    # so here is a faster Doubly Linked List that I am taking notes on : 

    class Node: 

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    class LRUCache:

        def __init__(self, capacity):
            self.capacity = capacity            # capacity of the cache.
            self.cache = {}                     # dict for tracking bodes in cache.
            self.head = Node(0, 0)              # dummy head node.
            self.tail = Node(0, 0)              # dummy tail node.
            self.head.next = self.tail          # connect head to tail forwards.
            self.tail.prev = self.head          # connect tail to head backwards.

        def remove(self, node):
            prev = node.prev                    # grabs prev node to cur node.
            nxt = node.next                     # grabs next node to cur node.
            prev.next = nxt                     # connects prev to next forwards.
            nxt.prev = prev                     # connects next to prev backwards.

            # node is now removed.

        def add(self, node):
            node.prev = self.head               # connects new node to dummy head backwards.
            node.next = self.head.next          # connects new node to last MRU node forwards.
            self.head.next.prev = node          # connects current MRU node to new node backwards.
            self.head.next = node               # connects dummy head to new node forwards.

            # node is now MRU.

        def get(self, key): 
            if key in self.cache:               # if key is in cache.
                node = self.cache[key]          # grab node from cache.
                self.remove(node)               # remove node from list.
                self.add(node)                  # add node to the front of the list.    
                return node.value               # return the value of the node.
            else:
                return -1                       # if key is not in cache, return -1.

        def put(self, key, value):
            if key in self.cache:               # if key is in cache.
                self.remove(self.cache[key])    # remove node from list.

            # either way if node in cache or not, we are adding new node.

            node = Node(key, value)             # create new node.
            self.add(node)                      # add node to front, now becomes MRU.
            self.cache[key] = node              # add node to cache.
            if len(self.cache) > self.capacity: # if cache is over capacity.
                last = self.tail.prev           # grab last node.
                self.remove(last)               # remove node from list.
                del self.cache[last.key]        # remove node from cache.