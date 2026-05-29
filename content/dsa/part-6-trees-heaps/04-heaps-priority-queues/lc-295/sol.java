// LC 295. Find Median from Data Stream
// Two-heap technique: lower half max-heap (reverseOrder); upper half min-heap.
import java.util.Comparator;
import java.util.PriorityQueue;

public final class Sol {
    public static class MedianFinder {
        private final PriorityQueue<Integer> lower =
            new PriorityQueue<>(Comparator.reverseOrder());      // max-heap
        private final PriorityQueue<Integer> upper = new PriorityQueue<>();   // min-heap

        public void addNum(int num) {
            lower.offer(num);
            upper.offer(lower.poll());                  // ordering invariant
            if (upper.size() > lower.size()) {
                lower.offer(upper.poll());              // size invariant
            }
        }

        public double findMedian() {
            if (lower.size() > upper.size()) {
                return lower.peek();
            }
            return (lower.peek() + upper.peek()) / 2.0;     // float division mandatory
        }
    }
}
