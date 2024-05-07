// https://leetcode.com/problems/reverse-linked-list/
// 05 / 07 / 2024 - 2:36 pm
// sol - work backwards with an empty node.
// easy
// run-time -> 100.00%
// memory -> 92.18%

class reverseList {

    // O(n) Approach. - 05 / 07 / 2024 - 2:36 pm
    // Didn't understand problem very well so I had to find a video explaining the process of reversal.
    // Had the right idea however did not know how to properly return. 
    // In this approach,
    // Set Cur = Head, and While Cur is Not the Null Node (End of List)
    // Save Next Val. Set Cur Next to Prev. Move Prev Over to Cur. Move Cur over to Next.
    // Then Repeat and Return Prev once Null.
    // RT - 100.00%, MEM - 92.18%
    public ListNode reverseListSquared(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode prev = null;

        ListNode cur = head; 
        while (cur != null) {
            ListNode tmp = cur.next; // Saving Next Cur Val to Tmp.
            cur.next = prev; // Setting Next Value from Cur Idx to Empty (Previous).
            prev = cur; // Moving Previous Over One.
            cur = tmp; // Moving Cur Over One.
        }
        return prev; // Return Empty b/c it is now Head of List.
    } 
}
