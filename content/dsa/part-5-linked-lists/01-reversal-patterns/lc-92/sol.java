// LC 92. Reverse Linked List II
// One-pass head-insertion variant: walk a sentinel (left-1) steps to
// land just before the segment, then for (right-left) iterations splice
// each newly-encountered node to the front of the reversed prefix.
public final class Sol {

    public static final class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    /** One-pass range reversal via head-insertion. Time O(n), space O(1). */
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        for (int i = 0; i < left - 1; i++) {
            pre = pre.next;
        }

        // `curr` is the first node of the segment to reverse; it stays put
        // and becomes the segment's tail. Each iteration lifts curr.next out
        // and splices it to the front of the reversed prefix.
        ListNode curr = pre.next;
        for (int i = 0; i < right - left; i++) {
            ListNode moved = curr.next;
            curr.next = moved.next;
            moved.next = pre.next;
            pre.next = moved;
        }

        return dummy.next;
    }
}
