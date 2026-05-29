# LC 509. Fibonacci Number
import sys
from functools import lru_cache


def fib(n: int) -> int:
    """LC 509: top-down memoization with an explicit dict.

    Time O(n), space O(n) for the memo plus O(n) recursion depth.
    """
    memo: dict[int, int] = {0: 0, 1: 1}

    def solve(k: int) -> int:
        if k in memo:
            return memo[k]
        memo[k] = solve(k - 1) + solve(k - 2)
        return memo[k]

    return solve(n)


# Idiomatic alternative with @lru_cache. Same recurrence; the decorator IS
# the memo. Two ways to spell the same algorithm; pick the one your team
# reads more easily.
@lru_cache(maxsize=None)
def fib_cached(n: int) -> int:
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


# DSH-04 (DSA Handbook code-idioms): bump CPython's default 1000-frame
# recursion limit ONCE at module top-level for any DP chapter where naive
# recursion can approach 1000 frames. Set it once; never per function.
sys.setrecursionlimit(10_000)
