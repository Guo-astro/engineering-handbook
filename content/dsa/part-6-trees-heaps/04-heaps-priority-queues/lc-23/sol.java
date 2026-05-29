// LC 23. Merge k Sorted Lists
// PriorityQueue with explicit Comparator.comparingInt avoids the
// overflow trap of (a, b) -> a.val - b.val on adversarial inputs.
import java.util.Comparator;
import java.util.PriorityQueue;

public final class Sol {
    public static class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int val) { this.val = val; }
        public ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>(
            Comparator.comparingInt(n -> n.val)
        );
        for (ListNode h : lists) {
            if (h != null) heap.offer(h);
        }
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            tail.next = node;
            tail = node;
            if (node.next != null) {
                heap.offer(node.next);
            }
        }
        tail.next = null;
        return dummy.next;
    }
}
