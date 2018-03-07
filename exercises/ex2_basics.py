"""
Exercise 2: Python Language Elements
BTI7541, Prof. Dr. René Müller

PART I: BASICS

Problem 1: Implement a the function make_tower that returns
True if a tower of exact height can be built out of at most
num_small_bricks (of height 1) and at most num_tall_bricks
(of height 5).

>>> make_tower(8, num_small_bricks=3, num_tall_bricks=1)
True
>>> make_tower(9, num_small_bricks=3, num_tall_bricks=1)
False
>>> make_tower(10, num_small_bricks=3, num_tall_bricks=2)
True
>>> make_tower(8, num_small_bricks=3, num_tall_bricks=2)
True
>>> make_tower(9, num_small_bricks=3, num_tall_bricks=2)
False
>>> make_tower(11, num_small_bricks=6, num_tall_bricks=1)
True
>>> make_tower(11, num_small_bricks=6, num_tall_bricks=0)
False
>>> make_tower(11, num_small_bricks=1, num_tall_bricks=4)
True
>>> make_tower(10, num_small_bricks=0, num_tall_bricks=3)
True
>>> make_tower(12, num_small_bricks=1, num_tall_bricks=4)
False
>>> make_tower(7, num_small_bricks=3, num_tall_bricks=1)
True
>>> make_tower(7, num_small_bricks=1, num_tall_bricks=1)
False
>>> make_tower(7, num_small_bricks=2, num_tall_bricks=1)
True
>>> make_tower(11, num_small_bricks=7, num_tall_bricks=1)
True
>>> make_tower(8, num_small_bricks=7, num_tall_bricks=1)
True
>>> make_tower(13, num_small_bricks=7, num_tall_bricks=1)
False
>>> make_tower(46, num_small_bricks=43, num_tall_bricks=1)
True
>>> make_tower(46, num_small_bricks=40, num_tall_bricks=1)
False
>>> make_tower(47, num_small_bricks=40, num_tall_bricks=2)
True
>>> make_tower(50, num_small_bricks=40, num_tall_bricks=2)
True
>>> make_tower(52, num_small_bricks=40, num_tall_bricks=2)
False
>>> make_tower(33, num_small_bricks=22, num_tall_bricks=2)
False
>>> make_tower(10, num_small_bricks=0, num_tall_bricks=2)
True
>>> make_tower(1000100, num_small_bricks=1000000, num_tall_bricks=1000)
True
>>> make_tower(100003, num_small_bricks=2, num_tall_bricks=1000000)
False
>>> make_tower(19, num_small_bricks=20, num_tall_bricks=0)
True
>>> make_tower(21, num_small_bricks=20, num_tall_bricks=0)
False
>>> make_tower(51, num_small_bricks=20, num_tall_bricks=4)
False
>>> make_tower(39, num_small_bricks=20, num_tall_bricks=4)
True

Problem 2: Implement a function that counts the number times value
'needle' occurs in the list 'haystack'.

>>> count_occurrence(1, [1, 2, 3])
1
>>> count_occurrence(4, [4, 1, 4, 2, 3, 4])
3
>>> count_occurrence(42, [])
0
>>> count_occurrence(42, [1, 2, 3, 4])
0
>>> count_occurrence(9, list(range(10)))
1
>>> count_occurrence(5, [5] * 10)
10
>>> count_occurrence(0, [x % 2 for x in range(10)])
5


Problem 3: Implement the fibonacci(num) that returns the first num
numbers of the Fibonacci sequence. The first two elements of
the Fibonacci sequences are 1, the subsequent numbers are
calculated as the sum of the previous two numbers of the
sequence.

>>> fibonacci(0)
[]
>>> fibonacci(1)
[1]
>>> fibonacci(2)
[1, 1]
>>> fibonacci(3)
[1, 1, 2]
>>> fibonacci(5)
[1, 1, 2, 3, 5]
>>> fibonacci(10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""


def make_tower(height, *, num_small_bricks, num_tall_bricks):
    """Returns True if a tower of `height` can be built out of at most
       num_small_bricks of height 1 and num_tall_bricks of height. """
    if height > num_small_bricks+num_tall_bricks*5:
       return False
    if height<=num_small_bricks:
       return True
    small_bricks_needed=height-num_tall_bricks*5
    if height//5<num_tall_bricks:
        small_bricks_needed=height%5
    if small_bricks_needed<=num_small_bricks:
        return True
    return False 


def count_occurrence(needle, haystack):
    """Returns the number of times value in 'needle' occurs in
       the list haystack."""
    found = 0
    for hay in haystack:
        if needle==hay:
            found+=1
    return found


def fibonacci(num):
    """Returns a list of the first num numbers of the Fibonacci sequence."""
    if num==0:
        return []
    if num==1:
        return [1]
    if num==2:
        return[1,1]
    fib=fibonacci(num-1)
    fib.append(fib[-1]+fib[-2])
    return fib

if __name__ == '__main__':
    import doctest
    doctest.testmod()