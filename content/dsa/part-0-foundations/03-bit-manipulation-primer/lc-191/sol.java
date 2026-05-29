// LC 191. Number of 1 Bits

public final class Sol {

    /** Brian Kernighan's loop. O(popcount(n)) time, O(1) space. */
    public static int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= n - 1; // clear the lowest set bit
            count++;
        }
        return count;
    }

    private Sol() {}
}
