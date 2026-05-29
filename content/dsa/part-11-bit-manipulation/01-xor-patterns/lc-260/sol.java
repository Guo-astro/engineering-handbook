// LC 260. Single Number III
//
// XOR all -> xor_all = a ^ b. Bucket by lowest differing bit. Two LC-136s.

public final class Sol {

    public static int[] singleNumber(int[] nums) {
        int xorAll = 0;
        for (int x : nums) {
            xorAll ^= x;
        }
        // Note: when xorAll == Integer.MIN_VALUE, -xorAll == Integer.MIN_VALUE
        // and the AND still yields the sign bit alone. Java's two's-complement
        // int overflow on negation is well-defined; the idiom works unchanged.
        int diffBit = xorAll & -xorAll;
        int a = 0, b = 0;
        for (int x : nums) {
            if ((x & diffBit) != 0) {
                a ^= x;
            } else {
                b ^= x;
            }
        }
        return new int[] {a, b};
    }

    private Sol() {}
}
