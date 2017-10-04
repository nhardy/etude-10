#!/usr/bin/env python3

"""
Étude 10 - Red and Green
Author(s): Nathan Hardy
"""

import cProfile
import functools
import math
import sys

from typing import Generator, Tuple

def get_nontrivial_near_factors(number: int) -> Generator[int, None, None]:
    """
    Generates all of the 'near factors' of a number
    """

    if number > 1:
        g = math.floor(math.sqrt(number))

        for potential in range(g + 1, number // 2 + 1):
            if number // (number // potential) == potential:
                yield potential

COUNTS = {}

def get_counts(number: int) -> Tuple[int, int]:
    if number == 1:
        return (1, 0)

    green, red = get_counts(number - 1)
    if get_colour(number) == 'G':
        return (green + 1, red)
    else:
        return (green, red + 1)

# Using a memoize cache for speedier repeated lookups
@functools.lru_cache(maxsize=None)
def get_colour(number: int) -> str:
    """
    Returns the 'colour' of a number
    """

    if number == 1:
        return 'G'

    green, red = get_counts(math.floor(math.sqrt(number)))

    counts = {
        'G': green,
        'R': red,
    }

    for near_factor in get_nontrivial_near_factors(number):
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

    for i in range(max(map(lambda s: s[1], scenarios))):
        get_counts(i)

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
        print(n, list(get_nontrivial_near_factors(n)))

    # print(get_counts(100))

    # print(get_colour(10))

    cProfile.run('main()')
    # main()
