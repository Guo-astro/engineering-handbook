// LC 142. Linked List Cycle II
public final class Sol {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int v) { this.val = v; }
    }

    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        // Phase 1: detect cycle existence.
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {  // pointer identity on reference types
                // Phase 2: locate cycle entry. Both pointers advance at speed 1.
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null;
    }
}
