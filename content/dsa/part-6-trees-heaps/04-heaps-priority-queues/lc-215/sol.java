// LC 215. Kth Largest Element in an Array
// heap solution mirrors
// top-K idiom. Quickselect lives at chapter 2.7; this is the heap alternative.
import java.util.PriorityQueue;

public final class Sol {
    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();   // min-heap by default
        for (int x : nums) {
            if (heap.size() < k) {
                heap.offer(x);
            } else if (x > heap.peek()) {
                heap.poll();
                heap.offer(x);
            }
        }
        return heap.peek();
    }
}
