#!/usr/bin/env python3

"""
Étude 10 - Red and Green
Author(s): Nathan Hardy
"""

import functools
import sys

def get_near_factors(number: int) -> list:
    # TODO: Get list of near factots
    return []

@functools.lru_cache(maxsize=None)
def get_colour(number: int, cache) -> str:
    if number == 1:
        return 'G'

    near_factors = get_near_factors(number)
    counts = {}
    for f in near_factors:
        colour = get_colour(f)

        if colour not in counts:
            counts[colour] = 0
        
        counts[colour] += 1

    return 'R' if counts['G'] > counts['R'] else 'G'

def main():
    for unstripped_line in sys.stdin.readlines():
        line = unstripped_line.strip()

        if line.startswith('#'):
            continue

        a, b = map(int, unstripped_line.split())

        # TODO
        print(a, b)

if __name__ == '__main__':
    main()
