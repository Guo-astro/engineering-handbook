# LC 150. Evaluate Reverse Polish Notation
from typing import List


def eval_rpn(tokens: List[str]) -> int:
    """Single-stack postfix evaluator. Truncate-toward-zero on division."""
    stack: List[int] = []
    for t in tokens:
        if t in ("+", "-", "*", "/") and len(t) == 1:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                # int(a / b) truncates toward zero; a // b would floor and break
                # 7 / -3 (LC expects -2; floor would give -3).
                stack.append(int(a / b))
        else:
            # Operand: handles negative literals like "-11" since the operator
            # branch above requires len(t) == 1.
            stack.append(int(t))
    return stack[0]
