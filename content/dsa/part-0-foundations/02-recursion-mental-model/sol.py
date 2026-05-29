# Chapter 0.2 — The recursion mental model
# Worked example: factorial(n) by direct recursion.
import sys

sys.setrecursionlimit(10**6)  # CPython default 1000 is too low for chapter exercises.


def factorial(n: int) -> int:
    """Return n! computed by direct recursion. Requires n >= 0."""
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    # Base case: 0! = 1 by definition. The recursion terminates here.
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)
