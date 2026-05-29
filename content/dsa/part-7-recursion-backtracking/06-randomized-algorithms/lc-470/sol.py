# LC 470. Implement Rand10 Using Rand7


def rand7() -> int:
    """Stub — interview problem provides this as a black box returning
    a uniform integer in 1..7. The real harness injects the LC version.
    """
    raise NotImplementedError


def rand10() -> int:
    """Two rand7 calls form 49 equally-likely outcomes. Accept the first
    40 (uniform on 1..40) and project onto 1..10; reject 41..49 and
    redraw. Expected calls per accepted sample = 2 * 49 / 40 = 2.45.
    """
    while True:
        # Map the 49 outcomes to 1..49 with no overlap; accept 1..40.
        roll = (rand7() - 1) * 7 + rand7()
        if roll <= 40:
            # 40 outcomes split evenly into 10 groups of 4 each.
            return ((roll - 1) % 10) + 1
        # roll in 41..49: reject and continue.
