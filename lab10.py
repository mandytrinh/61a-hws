#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            return StopIteration
        self.current += 1
        return self.current - 1

    def __iter__(self):
        self.current = self.start
        return self

##############
# Generators #
##############

def generator():
    print("Starting here")
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield")
        i += 1
        
        
def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"

###########
# Streams #
###########

class Stream:
    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def add_streams(s1, s2):
    "*** YOUR CODE HERE ***"
