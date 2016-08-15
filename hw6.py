# CS 61A Fall 2014
# Name:
# Login:

class VendingMachine(object):
    """A vending machine that vends some product for some price.
    >>> v = VendingMachine('candy', 10) #10 is the cost
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, cost):
        self.balance = 0
        self.stock = 0
        self.cost = cost
        self.product = product
        self.quantity = 0

    def vend(self):
        if self.stock == 0 and self.balance ==0:
            return 'Machine is out of stock.'

       # elif self.balance >= self.cost and self.stock ==0:
        #    bal = self.balance
         #   self.balance = 0
          #  return 'Machine is out of stock. Here is your ${0}'.format(bal)

        elif self.cost > self.balance:
            return 'You must deposit ${0} more'.format(self.cost - self.balance)

        elif self.balance == self.cost and self.stock !=0:
            self.stock = self.stock - 1
            self.balance = 0
            return 'Here is your candy.'

        elif self.balance > self.cost and self.stock !=0:
            self.stock = self.stock - 1
            net_bal = self.balance - self.cost
            self.balance = 0
            return 'Here is your candy and ${0} change'.format(net_bal)

    def deposit(self,dollar_amount):
        self.balance += dollar_amount
        if self.stock == 0: #tests if there is nothing, then rejects deposit
            bal = self.balance
            self.balance = 0
            return 'Machine is out of stock. Here is your ${0}.'.format(bal)
        return "Current balance: ${0}".format(dollar_amount)

    def restock(self,quantity):
        self.stock += quantity
        return "Current candy stock: {0}".format(self.stock)

v = VendingMachine('candy', 10)
print ("1", v.vend())
    #'Machine is out of stock.'
print('2', v.restock(2))
    #'Current candy stock: 2'
print ('3', v.vend())
    #You must deposit $10 more.'
print('4',v.deposit(7))
    #'Current balance: $7'
print ('5',v.vend())
    #'You must deposit $3 more.'
print( '6', v.deposit(5))
    #'Current balance: $12'
print ('7', v.vend())

    #'Here is your candy and $2 change.'
print('8', v.deposit(10))
    #'Current balance: $10'
print ('9', v.vend())
    #'Here is your candy.'
print('10', v.deposit(15))
    #'Machine is out of stock. Here is your $15.'


print ('*****************PROBLEM 2 BEGINS***********************')
#Problem 2

class MissManners(object):
    """A container class that only forward messages that say please.
    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    def __init__(self, parameter, *args):
        self.parameter = parameter

    def ask (self,request, *args):
        split_request = request.split()
        starts_with_please = ('please' == split_request[0])
        rest_of_request = ' '.join(split_request[1:])
        if not starts_with_please:
            return "You must learn to say please first."
        if hasattr(self.parameter, rest_of_request): #if there is an attribute in rest_of_request
            instance_function = getattr(self.parameter ,rest_of_request)
            result = instance_function(*args)
            return result
        else:
            return 'Thanks for asking, but I know not how to {0}'\
                    .format(rest_of_request)


            
                
        # elif request == 'please vend':
            # return getattr(VendingMachine,vend)
        # elif request == 'please deposit':
            # return getattr(vendingmachine,deposit)

v = VendingMachine('teaspoon', 10)
v.restock(2)
    #'Current teaspoon stock: 2'
m = MissManners(v)
print('1',m.ask('vend'))
    #'You must learn to say please first.'
print('2',m.ask('please vend'))
    #'You must deposit $10 more.'
print ('3',m.ask('please deposit', 20))
    #'Current balance: $20'
print ('4',m.ask('now will you vend?'))
    #'You must learn to say please first.'
print ('5',m.ask('please hand over a teaspoon'))
    #'Thanks for asking, but I know not how to hand over a teaspoon'
print ('6',m.ask('please vend'))
    #'Here is your teaspoon and $10 change.'
really_fussy = MissManners(m)
print ('7',really_fussy.ask('deposit', 10))
    #'You must learn to say please first.'
print ('8',really_fussy.ask('please deposit', 10))
    #'Thanks for asking, but I know not how to deposit'
print ('9',really_fussy.ask('please please deposit', 10))
    #'Thanks for asking, but I know not how to please deposit'
print('10',really_fussy.ask('please ask', 'please deposit', 10))
    #'Current balance: $10'
fussy_three = MissManners(3)
print('11',fussy_three.ask('add', 4))
    #'You must learn to say please first.'
print ('12',fussy_three.ask('please add', 4))
    #'Thanks for asking, but I know not how to add'
print ('13',fussy_three.ask('please __add__', 4))
    #7

##########################################
#           Challenge Problem            #
# (You can delete this part if you want) #
##########################################

def make_instance(some_class):
    """Return a new object instance of some_class."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = some_class['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
    """Return value or a bound method if value is callable."""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

def make_class(attributes, base_classes=()):
    """Return a new class with attributes.
    attributes -- class attributes
    base_classes -- a sequence of classes
    """
    "*** YOUR CODE HERE ***"

def init_instance(some_class, *args):
    """Return a new instance of some_class, initialized with args."""
    instance = make_instance(some_class)
    init = some_class['get']('__init__')
    if init:
        init(instance, *args)
    return instance

# AsSeenOnTVAccount example from lecture.

def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""

    interest = 0.02

    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')

    return make_class(locals())

Account = make_account_class()

def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee.
    >>> checking = CheckingAccount['new']('Jack')
    >>> checking['get']('interest')
    0.01
    >>> checking['get']('deposit')(20)
    20
    >>> checking['get']('withdraw')(5)
    14
    """
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)

    return make_class(locals(), [Account])

CheckingAccount = make_checking_account_class()

def make_savings_account_class():
    """Return the SavingsAccount class, which imposes a $2 deposit fee.
    >>> savings = SavingsAccount['new']('Jack')
    >>> savings['get']('interest')
    0.02
    >>> savings['get']('deposit')(20)
    18
    >>> savings['get']('withdraw')(5)
    13
    """
    deposit_fee = 2

    def deposit(self, amount):
        fee = self['get']('deposit_fee')
        return Account['get']('deposit')(self, amount - fee)

    return make_class(locals(), [Account])

SavingsAccount = make_savings_account_class()

def make_as_seen_on_tv_account_class():
    """Return an account with lots of fees and a free dollar.
    >>> such_a_deal = AsSeenOnTVAccount['new']('Jack')
    >>> such_a_deal['get']('balance')
    1
    >>> such_a_deal['get']('interest')
    0.01
    >>> such_a_deal['get']('deposit')(20)
    19
    >>> such_a_deal['get']('withdraw')(5)
    13
    """
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 1)

    return make_class(locals(), [CheckingAccount, SavingsAccount])

AsSeenOnTVAccount = make_as_seen_on_tv_account_class()

