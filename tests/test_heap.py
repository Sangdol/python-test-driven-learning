import pytest
from heapq import heappush, heappop, heappushpop, heapreplace, heapify


# https://docs.python.org/3/library/heapq.html
def test_heapq():
    """
    This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.

    heapq, aka priority queue.
    It's a min heap.
    heapsort is not stable.
    """
    h = []
    heappush(h, 3)
    heappush(h, 2)
    heappush(h, 1)

    assert h == [1, 3, 2]
    assert heappop(h) == 1

    assert h == [2, 3]
    assert heappushpop(h, 0) == 0

    assert h == [2, 3]
    assert heapreplace(h, -1) == 2

    assert h == [-1, 3]


def test_heapq_tuples():
    """
    heap APIs will use the first element of tuples for sorting.
    https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
    """
    h = [(1, 'a'), (2, 'b'), (3, 'c')]
    heapify(h)

    assert heappop(h) == (1, 'a')
    assert heappop(h) == (2, 'b')
