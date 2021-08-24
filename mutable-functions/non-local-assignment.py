def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance # changes to the name balance will happen in the frame of make_withdraw
        if amount > balance:
            return 'insufficient funds'
        balance = balance - amount # re-bind balance in the first non-local frame in which it was bound previously
        return balance
    return withdraw

"""
# non-local assignments:
    @ effect: future assignments to that name change its pre-existing binding in the first non-local frame of the current environment in which that name is bound.
    @ py3 ref: names listed in a nonlocal statement must refer to pre-existing bindings in an enclosing scope. Names listed in a nonlocal statement must not collide with pre-existing bindings in the local scope.
"""

