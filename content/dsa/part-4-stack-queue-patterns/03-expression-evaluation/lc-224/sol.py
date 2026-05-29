# LC 224. Basic Calculator
from typing import List


def calculate(s: str) -> int:
    """Sign-stack iterative evaluator for +/- with parentheses and unary minus.

    On '(', push (saved_result, saved_sign) and reset to a fresh frame.
    On ')', fold the inner result back: result = saved_result + saved_sign * result.
    """
    stack: List[int] = []
    result = 0
    num = 0
    sign = 1  # +1 or -1
    for ch in s:
        if ch.isdigit():
            num = num * 10 + (ord(ch) - ord("0"))
        elif ch == "+":
            result += sign * num
            num = 0
            sign = 1
        elif ch == "-":
            result += sign * num
            num = 0
            sign = -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * num
            num = 0
            result *= stack.pop()  # the saved sign
            result += stack.pop()  # the saved running result
        # whitespace: skip
    result += sign * num
    return result
