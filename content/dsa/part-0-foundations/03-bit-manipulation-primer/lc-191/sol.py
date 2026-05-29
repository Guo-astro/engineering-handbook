# LC 191. Number of 1 Bits


def hamming_weight(n: int) -> int:
    """Count set bits via Brian Kernighan's loop. O(popcount(n)) time, O(1) space."""
    count = 0
    while n:
        n &= n - 1  # clear the lowest set bit
        count += 1
    return count
