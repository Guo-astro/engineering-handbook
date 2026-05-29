// DynArr<T> — geometric-resize dynamic array reference template.
// Parameterized growth factor (growthNum / growthDen) for studying the
// amortized-O(1) push proof; tracks reallocation count. Not an LC problem.
import java.util.Arrays;

public final class Sol {

    public static final class DynArr<T> {
        private Object[] buf;
        private int size;
        private int cap;
        private final int growthNum;
        private final int growthDen;
        private int reallocs;

        public DynArr(int initialCap, int growthNum, int growthDen) {
            if (initialCap < 1) throw new IllegalArgumentException("initialCap must be >= 1");
            if (growthNum <= growthDen) throw new IllegalArgumentException("growth factor must be > 1");
            this.buf = new Object[initialCap];
            this.size = 0;
            this.cap = initialCap;
            this.growthNum = growthNum;
            this.growthDen = growthDen;
            this.reallocs = 0;
        }

        public int size() { return size; }
        public int capacity() { return cap; }
        public int reallocations() { return reallocs; }

        @SuppressWarnings("unchecked")
        public T get(int i) {
            if (i < 0 || i >= size) throw new IndexOutOfBoundsException("get out of range");
            return (T) buf[i];
        }

        public void push(T x) {
            if (size == cap) grow();
            buf[size] = x;
            size += 1;
        }

        private void grow() {
            // Ceiling division so factors like 9/8 still grow on small caps.
            // Long cast avoids overflow on (cap * growthNum) near Integer.MAX_VALUE.
            int newCap = (int) (((long) cap * growthNum + growthDen - 1) / growthDen);
            // Guard against rounding to a no-op (would loop forever on next push).
            if (newCap <= cap) newCap = cap + 1;
            buf = Arrays.copyOf(buf, newCap);
            cap = newCap;
            reallocs += 1;
        }
    }

    public static int[] simulate(int initialCap, int growthNum, int growthDen, int nPush) {
        DynArr<Integer> a = new DynArr<>(initialCap, growthNum, growthDen);
        for (int i = 0; i < nPush; i++) a.push(i);
        return new int[] { a.size(), a.capacity(), a.reallocations() };
    }

    private Sol() {}
}
