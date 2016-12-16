# We will be using the following implementation of immutable linked lists.
# Keep in mind that your code should not depend on the assumption that links are implemented as lists — preserve data abstraction!

empty = None

def link(first, rest=empty):
    return [first, rest]

def first(s):
    return s[0]

def rest(s):
    return s[1]

###################################

def link_to_list(lst):
    """Returns a list that contains the same elements as the
        linked list.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(r)
    [1, 2, 3]
    """

    if lst == empty:
        return [] 
    else:
        return [first(lst)] + link_to_list(rest(lst))

########################################

#Problem 2

def map_link(lst, f):
    """Maps f onto each element in the linked list.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(map_link(r, lambda x: x**2))
       [1, 4, 9]

    """
    if lst == empty:
        return []
    else:
        return link((first(lst)), map_link(rest(lst), f))     

##############################

def RegList_to_LinkList(lst):
    """turns a regular list into a linked list
    >>> RegList_to_LinkList([1,2,3])
    link(1, link(2, link(3, empty)))
    """

    def helper(L):
        if not L:
            return empty
        return link(L[0], helper(L[1:])) 

    return helper(lst)

# print(RegList_to_LinkList([1,2,3]))

###############################

def alternate(lst):
    """Returns a new linked list that contains every other element
            of the original.
    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(alternate(r))
    [1, 3]
    >>> r = link(1, link(2, link(3, link(4, empty))))
    >>> link_to_list(alternate(r))
    [1, 3]
    """
    alternated_elements = []
    removed_elements = []
    reg_lst = link_to_list(lst)
    i = 0
    while i < len(reg_lst):
        if i%2 == 0:
            element = reg_lst[i]
            alternated_elements.append(element)
        i = i + 1
    linked_alternated_elements = RegList_to_LinkList(alternated_elements)
    return linked_alternated_elements

# r = link(1, link(2, link(3, empty)))
# print(link_to_list(alternate(r)))
# r = link(1, link(2, link(3,link(4, link(5, empty))))) 
# print(link_to_list(alternate(r)))

###########################################

def filter(pred, lst):
    """Returns a new link that contains elements of lst that
    satisfy the predicate.

    >>> r = link(1, link(2, link(3, empty)))
    >>> link_to_list(filter_link(lambda x: x % 2 == 1, r))
    [1, 3]
    >>> r = link(1, link(2, link(3, link(4, empty))))
    >>> link_to_list(filter_link(lambda x: x % 3 == 1, r))
    [1, 4]
    """
    if lst == empty: return []
    elif pred(first(lst)):
        return link(first(lst)), filter(pred,rest(lst))
    else:
        return filter(pred, rest(lst))

##########################################
#             TREES REVIEW               #
##########################################
def tree(root, subtrees=[]):
    return [root] + list(subtrees)

def root(t):
    return t[0]

def subtrees(t):
    return t[1:]

def is_leaf(t):#check if t has no or empty subtrees
    return not subtrees(t)

#Question 1
#Implement a function contains, which takes a tree t and an element e. 
#contains will return True if t contains the element e, and False otherwise.


def contains(t, e):
    # return ( e == root(t)) or any(map(lamda tree: contains(tree, e), subtrees(t))
    if e == root(t):
        return True
    elif is_leaf(t):
        return False
    else:
        for tree in subtrees(t):
            if contains(tree,e):
                return True
    return False
                               
#################################
#Question 2

#Implement a function all_paths, which takes a tree t. 
#all_paths will return a list of paths from the root to each leaf.
# For example, consider the following tree:

#   5
# /  \
# 3   6
# / \
# 2  1

# Calling all_paths on this tree would return

# [[5, 3, 2],
# [5, 3, 1],
# [5, 6]    ]

def all_paths(t):

    if is_leaf(t):
        return [[root(t)]]
    else:
        total = []
        for tree in subtrees(t):
            for path in all_paths(tree):
                total.append([root(t)] + path)
        return total 

##################################################
#           Object Oriented Programming         #
#################################################

# Write a Chef class with the following qualities:
# 
# Each Chef is initialized with a list of required ingredients. Each item in the list is added to a storage that is shared by all the Chefs with an initial stock of 2. If the item is already in the storage, do NOT add it in again.
# Each Chef can fetch_ingredients from a storage that is shared by all the Chefs. Each Chef only needs 1 of each ingredient.
# Each Chef can serve, where they put their finished food in a shared list of finished foods.

# >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
# >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
# >>> ramsay.cook()
# 'Not enogh ingredients!'
# >>> ramsay.serve()
# 'No food to serve!'
# >>> ramsay.fetch_ingredients()     # 1 salt remaining
# "Fetched: ['meat', 'bbq sauce', 'salt']"
# >>> ramsay.cook()
# 'Cooked steak!'
# >>> ramsay.serve()
# >>> Chef.finished
# ['steak']
# >>> albert.fetch_ingredients()     # 0 salt remaining
# "Fetched: ['egg', 'cheese', 'cream', 'salt']"
# # >>> albert.cook()
# 'Cooked quiche!'
# >>> albert.serve()
# >>> Chef.finished
# ['steak', 'quiche']
# >>> ramsay.fetch_ingredients()
# 'No more salt!'
# """

class Chef:
    storage = {}
    finished = []

    def __init__(self, entree, food_list):
        self.fetched = False
        self.cooked = False
        self.food_list, self.entree = food_list, entree
        for each_item in self.food_list:
            if each_item not in storage:
                Chef.storage[each_item] = 2
    
    def fetch_ingredients(self):
        for each_item in self.food_list:
            if Chef.storage[each_item] == 0:
                return "No more" + each_item + "!"
            Chef.storage[each_item] -= 1
        self.fetched = True
        return "Fetched: " + str(self.food_list)        

    def cook(self):
        if self.fetched == False:
            return "Not enough ingredients!"
        else:
            self.cooked = True
            self.fetched = False
            return "Cooked{0}!".format(self.entree)

    def serve(self):
        if self.cooked == False:
            return "No food to serve!"
        else:
            Chef.finished.append(self.entree)
        self.cooked = False

##################################################
#              MUTABLE LINKED LISTS             #
#################################################

class Link(object):
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

    def __repr__(self):
        if self.rest is empty:
            return 'Link({})'.format(repr(self.first))
        return 'Link({}, {})'.format(repr(self.first),
                                      repr(self.rest))

# Implement a function seq_to_link, which takes any type of sequence (e.g. tuple, list) and converts it to a Link.
	
    # """Converts SEQ into an Link.
    # >>> seq = [1, 2, 3, 4]
    # >>> seq_to_link(seq)
    # Link(1, Link(2, Link(3, Link(4))))
    # >>> null = ()
    # >>> seq_to_link(null) is Link.empty
    # True
    # """
def seq_to_link(seq):
    if not seq:
        return Link.empty
    return Link(seq[0], seq_to_link(seq[1:]))

#iterative version:

def seq_to_link(seq):
    new_link = Link.empty
    for elem in seq[::-1]:
        new_link = Link(elem, new_link)
    return new_link


# Implement a function map_link, which takes a Link and a function fn, and applies fn to every element in the Link.
# map_link should mutate the Link — do not return a new one!

# >>> r = Link(1, Link(2, Link(3)))
# >>> map_link(lambda x: x*x, r)
# >>> r
# Link(1, Link(4, Link(9)))

def map_link(fn, lst): #lst is a Link list
    while lst is not Link.empty:
        lst = fn(lst.first)
        lst = lst.rest

#Implement a function validate, which takes a Link and returns True if the Link is valid.

def validate(lst):
    """Returns True if lst is a valid Link.

    >>> lst = Link(1, Link(2, Link(3)))
    >>> validate(lst)
    True
    >>> okay = Link(Link(1), Link(2))
    >>> validate(okay)
    True
    >>> bad = Link(1, 2)
    >>> validate(Link.empty)
    True
    """
    if lst is Link.empty:
        return True
    elif lst.rest is not Link.empty and type(lst.rest) != Link:
        return False
    else:
        return validate(lst.rest)

# Implement a function count, which takes a Link and another value, and counts the number of times that value is found in the Link

# >>> r = Link(3, Link(3, Link(2, Link(3))))
# >>> count(r, 3)
# 3
# >>> count(r, 2)
# 1

def count(r, value):
    counter = 0
    if r is Link.empty:
        return 0
    else:
        while r is not Link.empty:
            if r.first == value:
                counter += 1
            r = r.rest
        return counter

#Implement a function extend_link, which takes two Links, s1 and s2, and mutates s1 such that it contains the elements of s2 at its tail. 
# Do this mutatively — don't return anything! Also, make sure s2 itself does not get attached to s1. You may assume s1 always has at least one element.

# >>> s1 = Link(1)
# >>> s2 = Link(2, Link(3))
# >>> extend_link(s1, s2)
# >>> s1
# Link(1, Link(2, Link(3)))
# >>> s1.rest is not s2
# True

def extend_link(s1,s2):
    if s2 is Link.empty:
        return 
    elif s1.rest is Link.empty:
        s1.rest = Link(s2.first)
        extend_link(s1.rest, s2.rest)
    else:
        extend_link(s1.rest,s2)

##################################################
#               INTERFACES                      #
#################################################

class DoubleList(object):
    """See doctests for behavior.

    >>> d = DoubleList([1, 2, 3])
    >>> repr(d)
    'DoubleList([1, 2, 3])'
    >>> str(d)
    '[1, 1, 2, 2, 3, 3]'
    >>> d[2]
    2
    >>> d[3]
    2
    >>> d[4]
    3
    >>> len(d)
    6
    >>> d.append(4)
    >>> str(d)
    '[1, 1, 2, 2, 3, 3, 4, 4]'
    """
    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        return 'DoubleList(' + __repr__(self.lst) + ')'
    
    def __str__(self):
        rep = '['
        for each_elem in self.lst:
            rep += '{0}, {0}, '.format(each_elem)
        return rep[:-2] + ']' #this gets rid of the trailing ', ' at the end

    def __append__(self, item):
        return self.lst.append(item)

    def __len__(self):
        return 2 * len(self.lst)
    
    def __getitem__(self, index):
        return self.lst[index // 2] #floor division rounds DOWN

##################################################
#               Practice exams                   #
#################################################

class Lawyer(object):
    def __init__(self, s):
        if len(s) < 2:
            self.s = s
        else:
            self.s = Lawyer(s[2:])

    def __repr__(self):
        return 'Lawyer(' + repr(self.s) + ')'

    def think(self):
        if hasattr(self, 'decide'):
            return self.decide()
        while type(self.s) == Lawyer:
            self.s = self.s.s
        return self.s

class CEO(Lawyer):
    def decide(self):
        return 'Denied'

obama = Lawyer(['a','b', 'c'])
romney = CEO(['x', 'y', 'z'])


#The following is an object-oriented recursive list implementation:

class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList()

    def __repr__(self):
        f = repr(self.first)
        if self.rest is Rlist.empty:
            return 'Rlist({0})'.format(f)
        else:
            return 'Rlist({0}, {1})'.format(f, repr(self.rest))

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

#Implement a mutating_map method that takes in a function and applies it to each element in an Rlist.
#This method should mutate the list in place, replacing each element with the result of applying the function
#to it. Do not create any new objects. You may assume that the input Rlist contains at least one element.

    def mutating_map (self,fn ):

        self.first = fn(self.first )
        if self.rest != Rlist.empty :
            self.rest.mutating_map(fn)

###########################################

n = 3
def follow():
    sunshine = 10
    def x(n):
        nonlocal sunshine
        def y(fn):
            nonlocal sunshine
            sunshine = fn(sunshine) + n
            return sunshine
        sunshine += n
        return y
    return x(5)

rain = follow()
fall = rain(lambda x: x * n)

#####################################
#Mark is tired of having to dig around BearFacts to look up student information, so he wrote a script to create a
#dictionary of student info. However, when he did so, he was sleep-deprived. As such, he accidentally swapped
#the keys and the values! Now he’s stuck with a dictionary that maps any single piece of student information
#to the student’s login:

#>>> info['Eric Tzeng'] # info is mark's faulty dictionary
#'cs61a-ta'
#>>> info['eric.tzeng@berkeley.edu']
#'cs61a-ta'

#Mark is too tired to fix this, so you’ll have to do it for him. We’ll do this by writing a get_info function. It
#should take a student login string and a faulty info dictionary as its two arguments and return a list containing
#all of that student’s information. The returned list can contain a student’s information in any order, but it
#must contain all of the information for a student found in the faulty dictionary.
#>>> get_info('cs61a-ta', info)
#['Eric Tzeng', 'eric.tzeng@berkeley.edu']

#You may assume that no two students have duplicate information. However, you may not assume that names
#and emails are the only pieces of information stored in the dictionary.

def get_info(login, info_dict):
    """
    Retrieve student information based on the student's login, using the
    provided (faulty) info_dict.
    >>> mark_dict = {'Andrew Huang': 'cs61a-tf', 'awesomeandrew@example.com': 'cs61a-tf',
    ... 'Robert Huang': 'cs61a-td', 'coolrob42@example.com': 'cs61a-td'}
    >>> get_info('cs61a-td', mark_dict)
    ['Robert Huang', 'coolrob42@example.com'] # order doesn't matter
    >>> get_info('cs61a-tf', mark_dict)
    ['awesomeandrew@example.com', 'Andrew Huang'] # order doesn't matter
    """
	student_info_list = []
	for info, account in info_dict.item():
		if account == login:
			student_info_list.append(info)
	return student_info_list

#	Albert keeps all of his top secret information in a binary tree. This prevents the layperson from reading his
#data. However, well trained computer scientists (such as you) can still access his information.
#As a further layer of protection, Albert turns some of the nodes in his trees into Eert nodes. Eert nodes,
#which have Tree as their base class, are like normal Tree nodes, except they swap their left and right branches.
#(Albert settles for nothing less than the most advanced encryption techniques known to man.)
#(a) (3 pt) Complete the __init__ method for the Eert class on the next page. Make sure to use inheritance
#as much as possible. The Eert class should work as follows:
#>>> e = Eert("61A account info",
#... Tree("Username: cs61a-te"),
#... Tree("Password: imsocool"))
#>>> e.entry # unchanged
#"61A account info"
#>>> e.left.entry # swapped with right
#"Password: imsocool"
#>>> e.right.entry # sw
#"Username: cs61a-te"

class Tree(object):
	def __init__(self, entry, left=None, right=None):
		self.entry = entry
		self.left = left
		self.right = right
	def decrypt(self):


class Eert(Tree):
	def __init__(self, entry, left=None, right=None)
		Tree.__init__(self, entry, right, left) #this is switching the left and right returned values tree is called

##################################################

def miley(ray):
	def cy():
		def rus(billy):
			nonlocal cy
			cy = lambda: billy + ray
			return (1,billy)
		if len(rus(2)) == 1:
			return (3,4)
		else:
			return (cy(), 5)
	return cy()[1]
billy = 6
miley(7)
