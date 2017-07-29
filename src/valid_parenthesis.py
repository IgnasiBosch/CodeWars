"""
Write a function called validParentheses that takes a string of parentheses, and determines if the order of the
parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.

Examples:
validParentheses( "()" ) => returns true
validParentheses( ")(()))" ) => returns false
validParentheses( "(" ) => returns false
validParentheses( "(())((()())())" ) => returns true

All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'
"""


def valid_parentheses(string):
    result = 0
    for c in string:
        if c == '(':
            result += 1
        if c == ')':
            result -= 1
        if result < 0:
            return False
    return result == 0
