"""
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a
given series of numbers. You are provided with consecutive elements of an Arithmetic Progression.
There is however one hitch: Exactly one term from the original series is missing from the set of numbers which have
been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function find_missing (list) , list will always be at least 3 numbers. The missing term will never
be the first or last one.

Example :

find_missing([1,3,5,9,11]) == 7
PS: This is a sample question of the facebook engineer challenge on interview street. I found it quite fun to solve on
paper using math , derive the algo that way. Have fun!
"""


def _find_missing(sequence):
    diff = (sequence[-1] - sequence[0]) // len(sequence)
    for i, v in enumerate(sequence):
        if sequence[i + 1] - v != diff:
            return v + diff


def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)