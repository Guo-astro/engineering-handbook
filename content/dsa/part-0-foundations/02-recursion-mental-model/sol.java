// Chapter 0.2 — The recursion mental model
// Worked example: factorial(n) by direct recursion.
class Sol {
    static long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("factorial is undefined for n < 0");
        }
        // Base case: 0! = 1 by definition. The recursion terminates here.
        if (n == 0) {
            return 1L;
        }
        // Recursive case: n! = n * (n-1)!
        // Promote to long because 13! = 6,227,020,800 overflows int (2^31 - 1 = 2,147,483,647).
        return (long) n * factorial(n - 1);
    }
}
