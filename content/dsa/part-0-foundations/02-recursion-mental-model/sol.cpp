// Chapter 0.2 — The recursion mental model
// Worked example: factorial(n) by direct recursion.
#include <stdexcept>

long long factorial(int n) {
    if (n < 0) {
        throw std::invalid_argument("factorial is undefined for n < 0");
    }
    // Base case: 0! = 1 by definition. The recursion terminates here.
    if (n == 0) {
        return 1LL;
    }
    // Recursive case: n! = n * (n-1)!
    // Promote BEFORE the multiply: signed overflow on int is undefined behaviour.
    return static_cast<long long>(n) * factorial(n - 1);
}
