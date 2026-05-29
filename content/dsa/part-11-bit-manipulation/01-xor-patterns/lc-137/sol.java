// LC 137. Single Number II
//
// Per-bit count modulo 3: O(32n) = O(n) time, O(1) space.

public final class Sol {

    public static int singleNumber(int[] nums) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            int bitSum = 0;
            for (int x : nums) {
                bitSum += (x >> i) & 1;
            }
            if (bitSum % 3 != 0) {
                result |= 1 << i;
            }
        }
        return result;
    }

    private Sol() {}
}
