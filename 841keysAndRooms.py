# https://leetcode.com/problems/keys-and-rooms/
# medium

class firstAttempt:

    # 10 / 11 / 2025 - 3:21 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 18.04 - 93.75%

    # no chatgpt!!! well actually i did for syntax because i didn't know 
    # if you could append stuff to a set but i didn't even use that.

    # i mean i was pretty confused on this one for a bit, like i was
    # debating between like a hash map or just like checking a set's length
    # if we got all of the keys. but i realized we needed to recurse to properly
    # check all the keys per room. so then i used a visited array to keep
    # track of the rooms we visited. 

    # what it does is recurse through the rooms, check if we've visited them
    # if so continue to next idx, if not, we update the visited array and
    # then recurse through the keys in the room. then we just check
    # if we have any roooms we haven't visited, if so return false.

    def checkRooms(self, key, rooms, visited):
        newKeys = rooms[key]

        for key in newKeys:
            if visited[key] == True:
                continue

            visited[key] = True
            self.checkRooms(key, rooms, visited)
        
        return

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        keys = rooms[0]

        visited = [True] + ([False] * (len(rooms) - 1))

        for key in keys:
            visited[key] = True
            self.checkRooms(key, rooms, visited)

        if False in visited:
            return False

        return True