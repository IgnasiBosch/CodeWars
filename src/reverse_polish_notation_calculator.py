"""
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should
evaluate to 14.

Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 +
expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
"""

import operator


def calc(expr):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split():
        if token in operators:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(operators[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()


def _calc(expr):
    operators = ['+', '-', '/', '*']
    acc = []
    for c in expr.split():
        if c in operators:
            a = acc.pop(len(acc) - 2)
            b = acc.pop(len(acc) - 1)
            result = eval('{}{}{}'.format(a, c, b))
            acc.append(str(result))
            continue
        acc.append(c)
    return eval(acc[-1]) if len(acc) else 0
