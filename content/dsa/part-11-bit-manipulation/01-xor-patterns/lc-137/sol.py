# LC 137. Single Number II
#
# Per-bit count modulo 3: every other element contributes 0 (mod 3) to each
# bit position; only the unique element's bits survive. O(32n) = O(n) time,
# O(1) space. The three-state ones/twos accumulator is the same answer in
# fewer instructions and is harder to derive under interview pressure.
from typing import List


def single_number(nums: List[int]) -> int:
    """LC 137 — element appearing once when every other element appears three times."""
    result = 0
    for i in range(32):
        bit_sum = 0
        for x in nums:
            bit_sum += (x >> i) & 1
        if bit_sum % 3:
            # Bit i is set in the unique element. Mind the sign bit on i == 31.
            if i == 31:
                result -= 1 << 31
            else:
                result |= 1 << i
    return result
