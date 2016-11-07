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
        return link(first(lst)), filter(pred,rest(lst)))
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
#################################
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

Class Chef:
    storage = {}
    finished = []

    def __init__(self, entree, food_list):
        self.fetched = False
        self.cooked = False
        for food in food_list:
            if food not in storage:
                storage[food] = 2
    
    def fetched_ingredients(self):
        ingred = []
        for each_item in food_list:
            if each_item not in self.storage or self.storage[each_item] == 0:
                return "No more {0}!".format(each_item)
            else:
                ingred.append(each_item)
                self.storage[each_item] -= 1
        self.fetched = True
        print "Fetched:{0}".format(ingred)        

    def cook(self):
        if self.fetched == False:
            return "Not enough ingredients!"
        else:
            self.cook = True
            return "Cooked{0}!".format(self.entree)

    def serve(self):
        if self.cook == False:
            return "No food to serve!"
        else:
            self.finished.append(entree)

