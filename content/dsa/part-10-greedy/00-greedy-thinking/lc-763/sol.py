# LC 763. Partition Labels
def partition_labels(s: str) -> list[int]:
    """LC 763: greedy boundary extension to last-occurrence index.

    One pre-pass to record the last index of each character; one
    main pass that extends the current partition's right boundary
    to the rightmost last-index of any character seen so far.
    Whenever the cursor reaches that boundary, the partition is
    closed. Time O(n), space O(1) (alphabet bound 26).
    """
    last = {c: i for i, c in enumerate(s)}
    parts: list[int] = []
    start = 0
    end = 0
    for i, c in enumerate(s):
        if last[c] > end:
            end = last[c]
        if i == end:
            parts.append(end - start + 1)
            start = i + 1
    return parts
