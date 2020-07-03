from . import Stack


SYMBOLS_PAIRS = {"(": ")", "[": "]", "{": "}"}


def is_balanced(symbols_string):
    openers = SYMBOLS_PAIRS.keys()
    my_stack = Stack()

    for symbol in symbols_string:
        if symbol in openers:
            my_stack.push(symbol)
            continue

        last_opened = my_stack.pop()
        if symbol != SYMBOLS_PAIRS[last_opened]:
            return False

    return my_stack.is_empty()
