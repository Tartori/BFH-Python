"""Performance comparison between class-based counter and
   factory function-based counter using the 'timeit' profiling
   library.
"""

import sys
import timeit


def make_counter():
    """Factory function returns a counter function with a private count."""
    count = 0

    def counter():
        """Counter function returns the post-increment value."""
        nonlocal count
        count += 1
        return count
    return counter


class Counter:
    """Class-based Counter."""
    def __init__(self):
        self._count = 0

    def __call__(self):
        """Callable increments the counter and returns the post-increment value."""
        self._count += 1
        return self._count


def do_profile():
    """Profiles the factory function-based and class-based counter."""
    print(sys.version)    # print the version information of the Python interpreter
    repetitions = 10_000_000
    print(f'Running counter() {repetitions} times...')
    factory_func_counter = timeit.timeit('counter()',
                                         setup='from counter_perf import make_counter; counter = make_counter()',
                                         number=repetitions)
    class_counter = timeit.timeit('counter()',
                                  setup='from counter_perf import Counter; counter = Counter()',
                                  number=repetitions)
    print('Factory Function-based Counter: {:.3f} ns/call (avg)'.format(factory_func_counter/repetitions*1e9))
    print('Class-based Counter:            {:.3f} ns/call (avg)'.format(class_counter/repetitions*1e9))


if __name__ == '__main__':
    do_profile()