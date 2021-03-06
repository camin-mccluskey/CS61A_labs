## Generators

def ints_to(n):
    for i in range(1, n + 1):
          yield i

def ints_to_5():
    for item in ints_to(5):
        yield item


def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def ints_to(n):
    ...     for i in range(1, n + 1):
    ...          yield i
    ...
    >>> def ints_to_5():
    ...     for item in ints_to(5):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(ints_to_5):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    1
    Next Generator:
    1
    2
    Next Generator:
    1
    2
    3
    Next Generator:
    1
    2
    3
    4
    Next Generator:
    1
    2
    3
    4
    5
    """
    def call_g(n):
        # number of times we should yield g()
        lst = list(g())
        desired = lst[:n]
        for i in desired:
            yield i

    num_generators = len(list(g()))
    for i in range(1,num_generators+1):
        yield call_g(i)


def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if type(lst) != list:
        lst = list(lst)
    if not lst:
        yield []
    else:
        for perm in permutations(lst[1:]):
            for i in range(len(lst)):
                yield perm[:i] + lst[0:1] + perm[i:]
