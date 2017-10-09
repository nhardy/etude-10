#!/usr/bin/env python3

"""
Étude 10 - Red and Green
Author(s): Nathan Hardy
"""

import functools
import sys
from typing import Generator

def get_near_factors(number: int) -> Generator[int, None, None]:
    """
    Generates all of the 'near factors' of a number
    """

    if number > 1:
        seen = set()
        divisor = number

        while divisor >= 2:
            near_factor = number // divisor
            if near_factor not in seen:
                seen.add(near_factor)
                yield near_factor

            divisor = number // (near_factor + 1)

# Using a memoize cache for speedier repeated lookups
@functools.lru_cache(maxsize=None)
def get_colour(number: int) -> str:
    """
    Returns the 'colour' of a number
    """

    if number == 1:
        return 'G'

    counts = {
        'G': 0,
        'R': 0,
    }

    for near_factor in get_near_factors(number):
        counts[get_colour(near_factor)] += 1

    return 'R' if counts['G'] > counts['R'] else 'G'

def main():
    """
    Main program
    """

    scenarios = []

    for unstripped_line in sys.stdin.readlines():
        line = unstripped_line.strip()

        # Ignore comments
        if line.startswith('#'):
            continue

        # Skip empty lines
        if line == '':
            continue

        # Add tuple(a, b) to the list of scenarios
        scenarios.append(tuple(map(int, unstripped_line.split())))

    print('\n\n'.join([
        '{} {}\n# {}'.format(a, b, ''.join([
            get_colour(n) for n in range(a, a + b)
        ])) for a, b in scenarios
    ]))

if __name__ == '__main__':
    main()
