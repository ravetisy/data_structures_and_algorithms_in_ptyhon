import ctypes


class Array:

    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size

        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        #initialize each element
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < len(self)  # search inside array size
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self)
        self._elements[index] = value

    def clear(self, value):

        # clears the array by setting each elemtn to value, in out case to None
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:

    def __init__(self, theArray):
        self._arrayRef = theArray
        self._currIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._currIndex < len(self._arrayRef):
            entry = self._arrayRef[self._currIndex]
            self._currIndex += 1
            return entry
        else:
            raise StopIteration