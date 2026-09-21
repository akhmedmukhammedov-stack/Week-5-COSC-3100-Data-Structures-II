import ctypes


# Time: append amortized O(1)/worst O(n), get/set O(1); Space: O(n).
class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self._data = (ctypes.py_object * self.capacity)()

    def append(self, x) -> None:
        if self.size == self.capacity:
            new_capacity = self.capacity * 2
            new_data = (ctypes.py_object * new_capacity)()
            for index in range(self.size):
                new_data[index] = self._data[index]
            self._data = new_data
            self.capacity = new_capacity
        self._data[self.size] = x
        self.size += 1

    def _check_index(self, i):
        if not isinstance(i, int):
            raise TypeError('Index must be an integer')
        if not 0 <= i < self.size:
            raise IndexError('Index out of range')

    def get(self, i):
        self._check_index(i)
        return self._data[i]

    def set(self, i, x) -> None:
        self._check_index(i)
        self._data[i] = x


if __name__ == '__main__':
    array = DynamicArray()
    for operation in (lambda: array.get(0), lambda: array.set(0, 1)):
        try:
            operation()
            raise AssertionError('Expected IndexError')
        except IndexError:
            pass
    for value in range(9):
        array.append(value)
    assert array.size == 9 and array.capacity == 16
    assert [array.get(i) for i in range(9)] == list(range(9))
    array.set(4, None)
    assert array.get(4) is None and array.get(5) == 5
    for index in (-1, 9):
        for operation in (lambda: array.get(index), lambda: array.set(index, 0)):
            try:
                operation()
                raise AssertionError('Expected IndexError')
            except IndexError:
                pass
    print('Challenge 7: all tests passed')
