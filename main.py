#!/usr/bin/env python3

"""
Étude 10 - Red and Green
Author(s): Nathan Hardy
"""

import cProfile
import functools
import sys

from typing import Generator

def get_near_factors(number: int) -> Generator[int, None, None]:
    """
    Generates all of the 'near factors' of a number
    """

    for potential in range(1, number // 2 + 1):
        if number // (number // potential) == potential:
            yield potential

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

    for (i, (a, b)) in enumerate(scenarios):
        if i == 0:
            print('\n')
        print(a, b)
        print('# ', end='')
        for n in range(a, a + b):
            print(get_colour(n), end='')
        print()

if __name__ == '__main__':
    for n in range(1, 20):
        print(n, list(get_near_factors(n)))

    cProfile.run('main()')
    # main()
