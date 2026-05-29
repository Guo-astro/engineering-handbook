// LC 50. Pow(x, n)

// Binary exponentiation. O(log |n|) time, O(1) space.
double myPow(double x, int n) {
    // Promote to long long: -INT_MIN is signed overflow (UB) on 32-bit int.
    long long m = n;
    if (m < 0) {
        x = 1.0 / x;
        m = -m;
    }
    double result = 1.0;
    double base = x;
    while (m > 0) {
        if (m & 1) {
            result *= base;
        }
        base *= base;
        m >>= 1;
    }
    return result;
}
