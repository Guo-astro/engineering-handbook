// LC 371. Sum of Two Integers

public class Solution {
    public int getSum(int a, int b) {
        // sum-without-carry: a ^ b
        // carry: (a & b) << 1
        // Java int is 32-bit two's complement; overflow wraps cleanly.
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
