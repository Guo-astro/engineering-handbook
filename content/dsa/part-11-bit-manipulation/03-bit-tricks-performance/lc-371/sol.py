# LC 371. Sum of Two Integers

def get_sum(a: int, b: int) -> int:
    """Return a + b without using + or -.

    Implements full-adder logic with bit-parallel composition:
      sum-without-carry: a XOR b
      carry:             (a AND b) << 1
    Iterate until carry is zero.

    Python ints are arbitrary-precision, so we mask to 32 bits each step
    and reinterpret the sign at the end. LeetCode's constraint is
    -1000 <= a, b <= 1000, well within 32-bit two's complement.
    """
    MASK = 0xFFFFFFFF
    SIGN_BIT = 0x80000000

    while b & MASK:
        carry = ((a & b) << 1) & MASK
        a = (a ^ b) & MASK
        b = carry

    # If the high bit is set, interpret as a negative 32-bit int.
    return a if a < SIGN_BIT else a - (SIGN_BIT << 1)
