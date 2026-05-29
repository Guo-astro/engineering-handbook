// LC 206. Reverse Linked List
public final class Sol {

    public static final class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    /** Iterative: prev/curr/next three-pointer rewire.
     *  Time O(n), space O(1). */
    public ListNode reverseListIterative(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    /** Recursive: invert the tail, then rewire head.next.next = head.
     *  Time O(n), space O(n) on the JVM stack. */
    public ListNode reverseListRecursive(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode newHead = reverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
