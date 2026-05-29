// LC 141. Linked List Cycle
public final class Sol {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int v) { this.val = v; }
    }

    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {  // pointer identity on reference types
                return true;
            }
        }
        return false;
    }
}
