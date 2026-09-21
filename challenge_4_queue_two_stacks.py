class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class _Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = _Node(value, self.head)

    def pop(self):
        if self.head is None:
            raise IndexError('Empty stack')
        value = self.head.value
        self.head = self.head.next
        return value

    def is_empty(self):
        return self.head is None


# Time: enqueue O(1), dequeue amortized O(1)/worst O(n); Space: O(n).
class QueueFromStacks:
    def __init__(self):
        # Python reserves "in", so its stack is named in_stack.
        self.in_stack = _Stack()
        self.out_stack = _Stack()

    def enqueue(self, x) -> None:
        self.in_stack.push(x)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        if self.out_stack.is_empty():
            raise IndexError('Empty queue')
        return self.out_stack.pop()


if __name__ == '__main__':
    q = QueueFromStacks()
    try:
        q.dequeue()
        raise AssertionError('Expected IndexError')
    except IndexError:
        pass
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    q.enqueue(4)
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [2, 3, 4]
    q.enqueue(None)
    assert q.dequeue() is None
    try:
        q.dequeue()
        raise AssertionError('Expected IndexError after draining')
    except IndexError:
        pass
    print('Challenge 4: all tests passed')
