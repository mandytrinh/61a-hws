# CS 61A Fall 2014
# Name:
# Login:

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <=3:
        return n
    else:
        return g(n-1)+2 * g(n-2)+3 * g(n-3)

#print (g(4))
#print (g(1))
#print (g(5))

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k == 0:
        return False
    elif k%10 == 7:
        return True
    else:
        return has_seven(k//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """


    def helper(e, k, dir_up):
        if e == n:
            return k
        if e % 7 == 0 or has_seven(e):
            if dir_up:
                return helper(e+1,k-1,False)
            return helper(e+1,k+1,True)
        elif not dir_up:
            return helper(e+1,k-1,False)
        else:
            return helper(e+1,k+1,True)
    return helper(1,1,True)


def is_power(k): #finds out if k is a power of 2
    if k == 1:
        return True
    while k > 1:
        if k%2 ==0:
            k = k//2
        else:
            return False
    return True
#print (is_power(6))
#print('---start count change---')
def count_change(n):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def is_power(k): #finds out if k is a power of 2
        if k == 1:
            return True
        while k > 1:
            if k%2 ==0:
                k = k//2
            else:
                return False
        return True


    def helper(x,part):
      if x == 0:
        return 1
      elif x < 0:
        return 0
      elif part <= 0:
        return 0
      elif x == 1: #base case
        return 1
      while not is_power(part):
        part = part - 1
        #print (x, part)
      return helper(x-part, part) + helper(x, part-1)
    return helper(n,n)


#print(count_change(7)) #should return 6
#print(count_change(10)) #14
#print(count_change(20)) #60
def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"



def any(a,b,pred):
    if b < a:
        return False
    elif pred(b):
        return True
    else:
        return any(a,b-1,pred)

print (any(1, 4, lambda x: x % 2 == 0))
print (any(-5, 2, lambda x: x * x == -3 * x))
print (any(1, 6, lambda x: x % 7 == 0))
print (any(0, 6, lambda x: x % 7 == 0))