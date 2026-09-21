class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Time: O(1) worst case per operation; Space: O(n), including auxiliary minima.
class MinStack:
    def __init__(self):
        self._values = None
        self._minima = None

    def push(self, x) -> None:
        minimum = x if self._minima is None else min(x, self._minima.value)
        # Linked stacks avoid resizing; both heads represent the same depth.
        self._values = _Node(x, self._values)
        self._minima = _Node(minimum, self._minima)

    def _require_nonempty(self):
        if self._values is None:
            raise IndexError('Empty stack')

    def pop(self) -> None:
        self._require_nonempty()
        self._values = self._values.next
        self._minima = self._minima.next

    def top(self):
        self._require_nonempty()
        return self._values.value

    def get_min(self):
        self._require_nonempty()
        return self._minima.value


if __name__ == '__main__':
    stack = MinStack()
    for operation in (stack.pop, stack.top, stack.get_min):
        try:
            operation()
            raise AssertionError('Expected IndexError')
        except IndexError:
            pass
    for value in (3, 5, 2):
        stack.push(value)
    assert stack.top() == 2 and stack.get_min() == 2
    stack.pop()
    assert stack.top() == 5 and stack.get_min() == 3
    stack.push(-1)
    stack.push(-1)
    stack.pop()
    assert stack.get_min() == -1
    stack.pop()
    assert stack.get_min() == 3
    print('Challenge 6: all tests passed')
