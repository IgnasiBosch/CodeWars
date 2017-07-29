"""
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger),
and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function:

simplify(poly)
that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients
(like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the
following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials,
so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english
alphabet.
"""

import re
import operator


def simplify(poly):
    operators = {'+': operator.add, '-': operator.sub}
    regex_global = r'((?:\+|\-)?(?:[0-9]{1,4})?[a-z]{1,4})'
    a = {}
    for block in re.findall(regex_global, poly):
        pb = parse_block(block)
        a.update({pb[0]: operators[pb[1]](a.get(pb[0], 0), pb[2])})
        # print(re.findall(regex_global, poly))
    print(a)


def print_block(block):
    pass


def parse_block(block):
    regex_block = r'(\+|\-)?([0-9]{1,4})?([a-z]{1,4})'
    re_block = re.findall(regex_block, block)[0]
    o = re_block[0] or '+'
    c = 1 if not len(re_block[1]) else int(re_block[1])

    return re_block[2], o, c
