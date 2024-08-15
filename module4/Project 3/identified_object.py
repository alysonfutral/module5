# resources used throughout code
# all powerpoint slides***
# Learning Python (O'Reilly) 4th ed.
# Python Crash Course 3rd/4th ed.
# Automate the Boring Stuff with Python (Al Sweigert)
# https://www.geeksforgeeks.org/read-only-properties-in-python/

# oid = object id
# r/o does not require setter

# use ABC "Abstract Base Class" Module
# https://www.geeksforgeeks.org/abstract-classes-in-python/
from abc import ABC, abstractmethod

class IdentifiedObject(ABC):

    @property
    def oid(self): #object id for this object
        return self._oid


    # initialization method that sets the
    # oid property as specified by the argument
    def __init__(self, oid):
        self._oid = oid


    # two IndentifiedObjects are equal if they
    # have the same type and the same oid
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.oid == other.oid

    # return hash code based on object's oid
    def __hash__(self):
        return hash(self.oid)
