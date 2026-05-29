// LC 50. Pow(x, n)

public final class Sol {

    /** Binary exponentiation. O(log |n|) time, O(1) space. */
    public static double myPow(double x, int n) {
        // Promote to long: -Integer.MIN_VALUE wraps in 32-bit two's complement.
        long m = n;
        if (m < 0) {
            x = 1.0 / x;
            m = -m;
        }
        double result = 1.0;
        double base = x;
        while (m > 0) {
            if ((m & 1) == 1) {
                result *= base;
            }
            base *= base;
            m >>= 1;
        }
        return result;
    }

    private Sol() {}
}
