"""
Benchmark for test the performance of Mako templates engine.
Includes:
    -two template inherences
    -HTML escaping, XML escaping, URL escaping, whitespace trimming
    -function defitions and calls
    -forloops
"""

import pyperf

import os

import fontmake.__main__

__author__ = "behdad@behdad.org (Behdad Esfahbod)"

def bench_func(filename):

    args = ['-o=variable', filename]

    fontmake.__main__.main(args)


if __name__ == "__main__":
    runner = pyperf.Runner()
    runner.metadata['description'] = (
        "Test the performance of the fontmake font compiler.")
    runner.metadata['fontmake version'] = fontmake.__version__

    # Get all our IO over with early.
    filename = os.path.join(os.path.dirname(__file__),
                            "data", "NotoSans-MM.glyphs")

    runner.bench_func('fontmake', bench_func, filename)
