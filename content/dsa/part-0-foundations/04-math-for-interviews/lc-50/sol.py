# LC 50. Pow(x, n)


def my_pow(x: float, n: int) -> float:
    """Binary exponentiation. O(log |n|) time, O(1) space."""
    if n < 0:
        x = 1.0 / x
        n = -n

    result = 1.0
    base = x
    while n > 0:
        if n & 1:
            result *= base
        base *= base
        n >>= 1
    return result
