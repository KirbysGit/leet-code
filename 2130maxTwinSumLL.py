# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# medium

class firstAttempt:

    # 09 / 28 / 2025 - 11:43 pm

    # Runtime -> 55 ms - 92.44%
    # Memory -> 41.43 MB - 65.43%

    # i had to use two hints and a tiny bit of chatgpt because my reverse logic was wrong.

    # but anyways, took me a minute to think, and then i used the hint because i was thinking bout
    # going through once getting length, then tracking the indexes with pairs like 0 3, 1 2, etc. 
    # but i knew that was overkill so i landed on the fast and slow pointer approach for landing
    # in the middle, then i was like okay now that i have that i just have to reverse the second
    # half, then iterate through each of the list adding the values and comparing the sums.

    # made sense, but i couldn't get my reverse logic to work, didn't realize how overkill my
    # previous solution for the reverse linked list was, like i was using three pointers and really only 
    # need the two. so chatgpt helped me with that, but after that it was all me. 

    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if not head.next.next:
            return head.val + head.next.val

        front = head
        middle = head
        back = head.next

        while back and back.next:
            middle = middle.next
            back = back.next.next
        
        prev = None
        middle = middle.next

        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp

        maxV = float('-inf')

        while prev:
            curPair = prev.val + head.val
            if curPair > maxV:
                maxV = curPair

            prev = prev.next
            head = head.next

        return maxV