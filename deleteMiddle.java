// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
// 05 / 07 / 2024 - 6:33 pm
// sol - fast and slow ptr
// medium
// best run-time -> 99.82%
// best memory -> 32.06%

class deleteMiddle {
    // First Attempt... 05 / 07 / 2024 - 6:33 pm
    // Count Length of List.
    // Take Length and find Mid from that.
    // Iterate through until Mid - 1.
    // Save Node.
    // When Mid, Delete Connection and Swap to Rest.
    // Else, Iterate through List.
    // RT - 24.04%, MEM - 79.63%
    public ListNode deleteMiddleFirst(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode cur = head;
        int counter = 0;

        while (cur != null) {
            counter++;
            cur = cur.next;
        }

        int middle = counter / 2;
        ListNode prev = head;
        cur = head;

        for (int i = 0; i < counter; i++) {
            if (i == middle - 1) {
                prev = cur;
                cur = cur.next;
            } else if (i == middle) {
                prev.next = cur.next;
                cur.next = null;
                cur = prev.next;
            } else {
                cur = cur.next;
            }
        }

        return head;
    }

    // Second Attempt... 05 / 07 / 2024 - 6:59 pm
    // One of the LeetCode Hints gave out that you can use a fast and slow ptr.
    // Trying to use this I implemented the approach below.
    // However because of all the if statements the code is very slow.
    // Trying to work around that now.
    // RT - 6.00%, MEM - 5.05%
    public ListNode deleteMiddleSecond(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = head;
        
        while (true) {
            System.out.println("Here!");
            if (fast.next == null) break;
            if (fast.next.next == null) {
                if (fast.next != null) {
                    prev = slow;
                    slow = slow.next;
                    break;
                }
            }
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        prev.next = slow.next;
        slow.next = null;

        return head;
    }

    // Third Attempt... 05 / 07 / 2024 - 7:12 pm
    // Basically the same as the previous approach except less repeated checks.
    // Added If statement after to basically handle the even vs odd cases.
    // RT - 99.82% , MEM - 32.06%
    public ListNode deleteMiddleThird(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = head;
        
        while (fast.next != null && fast.next.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        if (fast.next != null) {
            prev = slow;
            slow = slow.next;
        }

        prev.next = slow.next;
        slow.next = null;

        return head;
    }
}
