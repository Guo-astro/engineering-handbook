// LC 895. Maximum Frequency Stack
// A pop returns the most-frequent element pushed so far, ties broken by
// recency. Two parallel maps: count tracks current frequency per value;
// buckets[f] is the stack of values that have reached frequency f. A push
// at new count f appends to buckets[f] alone. A pop reads buckets[maxFreq],
// which delivers most-frequent and most-recent in one shot. O(1) per op.
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public final class FreqStack {

    private final Map<Integer, Integer> count = new HashMap<>();
    private final Map<Integer, Deque<Integer>> buckets = new HashMap<>();
    private int maxFreq = 0;

    public FreqStack() {}

    public void push(int val) {
        int f = count.merge(val, 1, Integer::sum);
        buckets.computeIfAbsent(f, k -> new ArrayDeque<>()).push(val);
        if (f > maxFreq) maxFreq = f;
    }

    public int pop() {
        int val = buckets.get(maxFreq).pop();
        count.merge(val, -1, Integer::sum);
        if (buckets.get(maxFreq).isEmpty()) {
            maxFreq--;
        }
        return val;
    }
}
