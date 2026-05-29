// LC 371. Sum of Two Integers

package main

func getSum(a int, b int) int {
    // Operate on uint32 to keep the bit pattern well-defined under shifts.
    ua, ub := uint32(a), uint32(b)
    for ub != 0 {
        carry := (ua & ub) << 1
        ua = ua ^ ub
        ub = carry
    }
    return int(int32(ua))
}
