# in CPython, lists are arrays of pointers

# inherits from a new-style object
# for usage: provides super(), @property, descriptors
# for class system: unify the concepts of class and type, makes type(x)
# typically the same as x.__class__
# old-style by default in Py2, new-style only in Py3
class StaticArray(Object):
    def __init__(self, length):
        self.store = [None] * length

    # O(1) for arr[i]
    def __getitem__(self, key):
        return self.__getattribute__(key)

    # O(1) for arr[i] = x
    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    # O(1) for del arr[i]
    def __delitem__(self, key):
        self.__delattr__(key)
