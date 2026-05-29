---
title: "Reversal patterns"
description: "Reverse a singly-linked list in place with prev, curr, next. The snapshot-then-clobber rule, plus the iterative and recursive forms that show up as a primitive in every later linked-list chapter."
slug: 01-reversal-patterns
part: 5
chapter: 1
difficulty: intermediate
prerequisites:
  - part-5-linked-lists/00-linked-list-fundamentals
  - part-0-foundations/02-recursion-mental-model
date_updated: 2026-05-24
languages: [python, java, cpp, go]
canonical_test: LC-206
widgets: [w-13-linked-list-pointer-rewiring]
ladder:
  core: [LC-206, LC-92, LC-234]
  stretch: [LC-143]
  star: LC-206
---

# Reversal patterns

A singly-linked list of five nodes, `1 -> 2 -> 3 -> 4 -> 5`. The interviewer wants the same nodes in opposite order, in one pass, with no extra storage past a constant number of pointers. The reader who has not seen the trick reaches for an array, copies values out, copies them back. Correct, but at `O(n)` extra space, and the interviewer's follow-up is "do it in `O(1)`."

That follow-up is the lesson. There is exactly one move that reverses a singly-linked list in place, and it relies on a small but unforgiving rule: the only pointer telling you where to go next is the same pointer you have to overwrite. Snapshot it, then clobber it. Get the order wrong by one line and the list either ends up with a single node or the runtime crashes on a null dereference.

## Why the obvious approach is not the right answer

LC 206 (Reverse Linked List) is the canonical signature problem. Input: the head of a list. Output: the head of the reversed list. Constraint: `0 <= n <= 5000`. The follow-up the problem statement asks every interviewee directly: "A linked list can be reversed either iteratively or recursively. Could you implement both?" The implicit question underneath is "and the iterative one in `O(1)` space, please."

The obvious approach is the array detour:

```python
# Brute force: O(n) time, O(n) extra space — what we are replacing
def reverse_brute(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    curr = head
    for v in reversed(values):
        curr.val = v
        curr = curr.next
    return head
```

Two passes, one array. It works. It also fails the chapter's follow-up: the array is `O(n)` extra space, and on a 5,000-node input the grader's space budget cares. Worse, the interviewer who asked for `O(1)` will simply say "do it without the array" and the reader who has only ever copied values out has nowhere to go.

The reason the array detour is wrong is structural. A singly-linked list does not let you walk backward. Every node knows the next node and nothing else. So if you want node 5 to point at node 4 in the reversed list, the *only* way to get there is to walk from 1 -> 2 -> 3 -> 4 -> 5 in the forward direction first, then perform the rewire on the way past. Now look at the rewire itself, on node 1. You want `n1.next = null` (n1 is going to be the new tail). But `n1.next` is the only pointer you have to n2; clobber it and the rest of the list disappears.

The fix is one extra local variable. Save `n1.next` into a register named `next` *before* you overwrite `n1.next = null`. That snapshot is what lets you keep walking. Three pointers total, never four. Sedgewick and Wayne teach the same loop in *Algorithms* §1.3; the CLRS exercise that asks for it formally is the standard reference.[^1]

## The pattern

Three local pointers — `prev`, `curr`, `next` — and four sub-steps per iteration. Each step does exactly one thing; the order is the algorithm.

```python
def reverse_list_iterative(head):
    prev, curr = None, head
    while curr is not None:
        nxt = curr.next        # 1. snapshot
        curr.next = prev       # 2. rewire (the only mutation)
        prev = curr            # 3. slide prev
        curr = nxt             # 4. slide curr
    return prev
```

**Solution** — Python ([Java](./01-reversal-patterns/lc-206/sol.java) · [C++](./01-reversal-patterns/lc-206/sol.cpp) · [Go](./01-reversal-patterns/lc-206/sol.go))

```python
# LC 206. Reverse Linked List
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """Iterative: prev/curr/next three-pointer rewire.

    Loop invariant on entry: every node strictly to the left of curr has been
    rewired so its next pointer goes one step backward; prev is the new head
    of that already-reversed prefix; the suffix starting at curr is unchanged.
    Time O(n), auxiliary space O(1).
    """
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursive: invert the tail, then rewire head.next.next = head.

    Recursion depth is O(n); CPython's default limit is 1000, so for n > ~900
    the caller must raise sys.setrecursionlimit() or use the iterative form.
    Time O(n), auxiliary space O(n) on the call stack.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

The loop invariant says the same thing the four sub-steps say in motion: on entry to each iteration, every node strictly to the left of `curr` has already been rewired backward, with `prev` heading the reversed prefix; the suffix from `curr` onward is structurally unchanged. The loop terminates when `curr` becomes `null`. The new head is whatever `prev` points at on exit. Time `O(n)` because every node is visited exactly once with `O(1)` work; auxiliary space `O(1)` because the only state outside the list is three local pointers.

> [!IMPORTANT]
> **Snapshot before clobber.** The four sub-steps are `snapshot, rewire, slide-prev, slide-curr`, in that order. Never write the rewire before the snapshot. The rewire destroys `curr.next`; without the snapshot, the next iteration reads `prev` instead of the original next node, the loop either terminates after one node or crashes on a null dereference, and the bug is invisible until the chapter's two-node test (`[1, 2]`) hits.

## Watch the rewire fire

The widget animates the LC 206 trace on `head = [1, 2, 3, 4, 5]` step-for-step. Twenty-three steps total: five iterations of the loop body, each split into the four sub-steps, plus three boundary states (init, loop-exit, return). Step through it once before reading on; the dependency between snapshot and mutation is faster to feel than to read.

> **Interactive widget:** [Linked list pointer rewiring](../widgets/w-13-linked-list-pointer-rewiring.yml) (panel `panel-b`) — rendered on the website; the YAML spec describes the keyframes.

*Pointer chips use the Wong palette: prev in sky blue, curr in orange, next in yellow. Reversed edges flip their direction-arrow render at the moment of rewire — steps 2, 6, 10, 14, 18 are the five mutations.*

The sub-step the widget makes most visible is step 2: `n1.next` flips from pointing at `n2` to pointing at `null`. That single edge mutation is the entire algorithm; everything else is bookkeeping. Watch the same pattern fire at steps 6, 10, 14, and 18, each time extending the reversed prefix by exactly one node. By step 18 the list is fully reversed; steps 19-22 are pure bookkeeping that drains the last iteration and returns `prev`.

## The recursive form, for the interviewer who asks for it

Same operation as a structural induction. Unwind to the tail; on the way back up, point each node's successor at the node itself.

```python
def reverse_list_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head      # the recursive rewire
    head.next = None           # clip the forward edge
    return new_head
```

The line `head.next.next = head` is the rewire. After the recursive call returns, `head.next` still points at what used to be `head`'s successor in the original list (the recursion did not mutate that edge on the way down); that successor's `next` should now point back at `head`, which is exactly `head.next.next = head`. Then `head.next = None` clips the forward edge so the tail of the new list terminates correctly. Skip the second line and the result is a list with a cycle: on `[1, 2, 3]`, `n2.next` still points to `n3` while `n3.next` now points to `n2`, so `n2 -> n3 -> n2 -> n3 -> ...` loops forever on any subsequent traversal.

The recursive form is `O(n)` time but `O(n)` *stack* space. That last bit is the gotcha. CPython's default `sys.getrecursionlimit()` is 1000, and LC 206's worst-case input has `n = 5000`. Submit the recursive form without raising the limit and the grader returns a `RecursionError` runtime crash, not a wrong answer.[^2] So in interviews where space matters, the iterative form is the canonical answer; the recursive form earns its place as the second mental model and as the answer to "show me both."

## Worked example: LC 92 (Reverse Linked List II)

LC 92 (Reverse Linked List II, Medium) extends the same rewire to a contiguous sub-range. Input: a list, plus 1-indexed positions `left` and `right`. Output: the list with positions `left .. right` reversed in place; positions outside that range untouched. The follow-up is "could you do it in one pass?"

On `head = [1, 2, 3, 4, 5], left = 2, right = 4`, the answer is `[1, 4, 3, 2, 5]`. Two challenges over LC 206: the head might or might not be inside the reversed segment (the `left == 1` case), and the segment has to re-attach to whatever sits to its left and right after the reversal.

The dummy-node sentinel from [Linked list fundamentals](./00-linked-list-fundamentals.md) handles the first challenge. Allocate one extra node at index 0 whose `next` points at the real head; now the "node before the segment" always exists, even when `left == 1`. The second challenge is solved by the one-pass head-insertion variant: walk a `pre` pointer to the node just before the segment, then for each iteration, lift the node sitting at `curr.next` out of its current position and splice it to the front of the reversed prefix. The first node of the segment stays put, and by the end has become the segment's tail.

```python
def reverse_between(head, left, right):
    if head is None or left == right:
        return head

    dummy = ListNode(0, head)
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next

    curr = pre.next
    for _ in range(right - left):
        moved = curr.next
        curr.next = moved.next
        moved.next = pre.next
        pre.next = moved

    return dummy.next
```

**Solution** — Python ([Java](./01-reversal-patterns/lc-92/sol.java) · [C++](./01-reversal-patterns/lc-92/sol.cpp) · [Go](./01-reversal-patterns/lc-92/sol.go))

```python
# LC 92. Reverse Linked List II
# One-pass head-insertion variant: walk a sentinel (left-1) steps to
# land just before the segment, then for (right-left) iterations splice
# each newly-encountered node to the front of the reversed prefix.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt


def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    """One-pass range reversal via head-insertion. Time O(n), space O(1)."""
    if head is None or left == right:
        return head

    dummy = ListNode(0, head)
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next  # type: ignore[assignment]

    # `curr` is the first node of the segment to reverse; it stays put and
    # becomes the segment's tail. Each iteration lifts curr.next out and
    # splices it to the front of the reversed prefix.
    curr = pre.next
    for _ in range(right - left):
        moved = curr.next
        curr.next = moved.next
        moved.next = pre.next
        pre.next = moved

    return dummy.next
```

Trace it on `[1, 2, 3, 4, 5], left = 2, right = 4`. After the sentinel walk, `pre` rests on node 1 and `curr` rests on node 2. The list still reads `dummy -> 1 -> 2 -> 3 -> 4 -> 5`.

Iteration 1. `moved = curr.next = 3`. Lift it out: `curr.next = moved.next = 4`. Splice it to the front of the reversed prefix: `moved.next = pre.next = 2`, then `pre.next = moved = 3`. The list now reads `dummy -> 1 -> 3 -> 2 -> 4 -> 5`. Node 2 has dropped one position; the reversed prefix is now `3 -> 2`.

Iteration 2. `moved = curr.next = 4` (curr is still 2; it never moves). Lift: `curr.next = 5`. Splice: `moved.next = pre.next = 3`, then `pre.next = 4`. The list reads `dummy -> 1 -> 4 -> 3 -> 2 -> 5`.

Two iterations because `right - left = 4 - 2 = 2`. The reversal runs in one pass over the segment, with the same `O(1)` auxiliary-space contract as LC 206. The doocs/leetcode reference solutions in Java, C++, and Go all follow this exact head-insertion shape; the four-language siblings up there mirror it.[^3]

## What it actually costs

| Variant | Time | Space | Notes |
|---|---|---|---|
| Iterative whole-list (LC 206) | `Theta(n)` | `O(1)` | The interview-default form. Three local pointers; one mutation per node. |
| Recursive whole-list (LC 206) | `Theta(n)` | `O(n)` stack | CPython ceiling at depth ~1000; LC's `n = 5000` hits the wall.[^2] |
| Range reversal one-pass (LC 92) | `O(n)` | `O(1)` | Sentinel walk to position `left - 1`, then `right - left` head-insertions. |
| Reversal-as-subroutine (LC 234, LC 143) | `O(n)` | `O(1)` | Find midpoint with fast/slow, reverse the back half, then either compare (LC 234) or merge (LC 143). |

The `O(1)` auxiliary-space bound on the iterative whole-list form is exactly the bound CLRS Exercise 10.2-7 *requires*: the exercise asks for a `Theta(n)`-time non-recursive procedure that reverses a singly-linked list "using no more than constant storage beyond that needed for the list itself."[^1] The three-local-pointer solution is the standard way to satisfy that. The same constraint propagates to LC 92 and to the reversal-as-subroutine pattern: every problem in the family inherits the `O(1)` ceiling because every problem reuses the same loop body.

## When the pattern bends

**Whole-list, iterative (LC 206).** The canonical form. No positional bookkeeping; the rewire applies uniformly from head to tail. The new head is whatever `prev` points at when the loop exits.

**Whole-list, recursive (LC 206 follow-up).** Same operation expressed as a structural induction. The mental model textbooks like; the runtime profile interview rubrics dislike. Use it when the interviewer asks for both forms; default to iterative when space matters.

**Sub-range, one-pass (LC 92).** The sentinel + head-insertion variant. Generalizes naturally to "reverse every K nodes"; that variant is LC 25 (Reverse Nodes in k-Group, Hard), which lives in [Reverse in groups of K](./02-reverse-in-groups-k.md) because the seam-management bookkeeping (counting `k`, reconnecting groups, handling the trailing remainder) is its own teachable unit.

**Reversal as a subroutine (LC 234, LC 143).** The reversal is a phase, not the whole algorithm. Find the midpoint with fast/slow pointers, reverse the second half in place, then either compare the two halves (LC 234, palindrome check) or interleave them into a single output (LC 143, reorder). The chapter on cycle detection picks up the fast/slow pointer scaffold; the chapter on merging linked lists picks up the interleave phase.

## Three pitfalls that bite

> [!WARNING]
> **Forgetting `head.next = None` on the recursive return.** After `head.next.next = head`, the original `head.next` edge has not been overwritten — the recursion did not mutate it on the way down. So `head.next` still points at the next node, while that next node now points back at `head`. Any subsequent traversal loops forever between the two. The fix is two paired lines on the return path: `head.next.next = head` first, then `head.next = None`. AlgoMonster's LC 206 editorial flags this as Common Pitfall #1.[^4]

> [!WARNING]
> **The LC 92 sentinel off-by-one.** With `left = 2`, the implementer wants `pre` to rest on node 1 (the node *before* the segment), but a natural `for _ in range(left)` loop matches the 1-indexed mental model and lands `pre` on node 2 instead — the first node *of* the segment. The subsequent splice rewires the wrong edge and the segment is reversed off-by-one, returning a wrong answer. The fix is `for _ in range(left - 1)`. The dummy node is the zeroth step, so the loop advances `left - 1` times, not `left`.

> [!WARNING]
> **Snapshot after mutation.** Writing `curr.next = prev` *before* `next = curr.next` is the canonical ordering bug. After the first rewire, `curr.next` no longer points at the original next node; it now points at `prev` (which is `null` on the first iteration). The next advance reads the wrong pointer, and the loop either terminates after one node or crashes with a null-pointer dereference. The four sub-steps must run in this exact order: `next = curr.next; curr.next = prev; prev = curr; curr = next`. Reading the loop body as four named sub-steps, with each one rendered separately by the widget, makes the dependency obvious.

## Problem ladder

### CORE (solve all three to claim chapter mastery)

- [LC 206 — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) [Easy] • linked-list-reversal-iterative-three-pointer ★
- [LC 92 — Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) [Medium] • sub-range-reversal-by-position
- [LC 234 — Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) [Easy] • linked-list-reversal-as-subroutine

### STRETCH (optional)

- [LC 143 — Reorder List](https://leetcode.com/problems/reorder-list/) [Medium] • linked-list-reversal-and-merge

LC 206 is the chapter's signature problem (★) and the one whose canonical test the four-language code panels pass. The CORE three span Easy/Medium only; the natural Hard variant, LC 25 (Reverse Nodes in k-Group), is owned by [Reverse in groups of K](./02-reverse-in-groups-k.md) because the seam-management bookkeeping is what makes it Hard. LC 234 is officially Easy on LC, but the optimal `O(1)`-space form combines three phases (midpoint via fast/slow, reverse the back half, walk in lockstep comparing) and reads closer to Medium for a first-time reader.

## Where this leads

[Reverse in groups of K](./02-reverse-in-groups-k.md) takes the loop body of LC 206 and runs it inside an outer counter. Same rewire, harder bookkeeping: count `k` nodes ahead, reverse them as a unit, splice the reversed group back into the surrounding list, repeat. The widget panel for that chapter shares the renderer and command vocabulary with this one; reading 5.0 -> 5.1 -> 5.2 in sequence advances the same widget through three difficulty levels.

The reversal-as-subroutine cousins lead elsewhere. The fast/slow midpoint scan that LC 234 and LC 143 lean on is its own pattern; that scaffold belongs to [Cycle detection and fast/slow pointers](./03-cycle-detection.md). The merge-alternately phase that closes out LC 143 generalizes to the merge of two sorted lists in [Merging linked lists](./04-merging-linked-lists.md).

## References

[^1]: Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*, 4th ed., MIT Press, 2022. §10.2, Exercise 10.2-7.

[^2]: Python 3 docs, `sys.setrecursionlimit`. <https://docs.python.org/3/library/sys.html#sys.setrecursionlimit>

[^3]: doocs/leetcode, LC 92 reference solutions. <https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0092.Reverse%20Linked%20List%20II/README_EN.md>

[^4]: AlgoMonster, LC 206 editorial. <https://algo.monster/liteproblems/206>
