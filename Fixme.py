#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    if n < 0:
        return []
    else:
        return [i * 2 for i in range(int((n / 2)) + 1)]
