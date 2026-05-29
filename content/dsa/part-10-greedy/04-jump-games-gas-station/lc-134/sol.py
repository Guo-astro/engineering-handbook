# LC 134. Gas Station
# Single-pass exchange-argument greedy: maintain running tank from a candidate
# start, reset to i+1 whenever the tank dips below zero, and use the
# unconditional total as the existence guard.
# O(n) time, O(1) space. Reference: Python only at this rung; Java/C++/Go
# four-language coverage deferred per research's verification log.
from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """LC 134. Find a start from which the circular tour completes, or -1."""
    total = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1
