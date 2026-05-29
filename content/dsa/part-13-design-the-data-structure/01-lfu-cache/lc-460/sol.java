// LC 460. LFU Cache
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;

class LFUCache {
    private final int cap;
    private int size;
    private int minFreq;
    private final Map<Integer, int[]> kvf;                  // key -> [val, freq]
    private final Map<Integer, LinkedHashSet<Integer>> fk;  // freq -> insertion-ordered keys

    public LFUCache(int capacity) {
        this.cap = capacity;
        this.size = 0;
        this.minFreq = 0;
        this.kvf = new HashMap<>();
        this.fk = new HashMap<>();
    }

    public int get(int key) {
        if (!kvf.containsKey(key)) return -1;
        int[] vf = kvf.get(key);
        int val = vf[0];
        int freq = vf[1];
        LinkedHashSet<Integer> bucket = fk.get(freq);
        bucket.remove(key);
        if (bucket.isEmpty()) {
            fk.remove(freq);
            if (minFreq == freq) minFreq++;
        }
        fk.computeIfAbsent(freq + 1, k -> new LinkedHashSet<>()).add(key);
        vf[1] = freq + 1; // mutate the int[] held by the map
        return val;
    }

    public void put(int key, int value) {
        if (cap <= 0) return;
        if (kvf.containsKey(key)) {
            kvf.get(key)[0] = value;
            get(key); // reuse promotion path
            return;
        }
        if (size == cap) {
            LinkedHashSet<Integer> bucket = fk.get(minFreq);
            int evictKey = bucket.iterator().next();
            bucket.remove(evictKey);
            if (bucket.isEmpty()) fk.remove(minFreq);
            kvf.remove(evictKey);
            size--;
        }
        kvf.put(key, new int[]{value, 1});
        fk.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
        minFreq = 1;
        size++;
    }
}
