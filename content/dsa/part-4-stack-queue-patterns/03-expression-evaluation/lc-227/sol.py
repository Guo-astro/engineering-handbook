# LC 227. Basic Calculator II
from typing import List


def calculate(s: str) -> int:
    """One-stack precedence-by-deferral evaluator.

    Defer + and - by pushing signed operands; apply * and / immediately by
    replacing the top of the stack. Final answer is sum(stack).
    """
    stack: List[int] = []
    num = 0
    op = "+"  # virtual leading operator
    n = len(s)
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + (ord(ch) - ord("0"))
        if (not ch.isdigit() and ch != " ") or i == n - 1:
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            else:  # '/'
                top = stack.pop()
                # int(top / num) truncates toward zero; // would floor.
                stack.append(int(top / num))
            num = 0
            op = ch
    return sum(stack)
