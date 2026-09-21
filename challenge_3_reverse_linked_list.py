from __future__ import annotations


class Node:
    def __init__(self, val, next: Node | None = None):
        self.val = val
        self.next = next


# Time: O(n), Space: O(1); existing nodes are reused.
def reverse_list(head: Node | None) -> Node | None:
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous


if __name__ == '__main__':
    assert reverse_list(None) is None
    single = Node(7)
    assert reverse_list(single) is single and single.next is None
    a, b, c = Node(1), Node(2), Node(3)
    a.next, b.next = b, c
    assert reverse_list(a) is c
    assert c.next is b and b.next is a and a.next is None
    assert reverse_list(c) is a
    assert a.next is b and b.next is c and c.next is None
    print('Challenge 3: all tests passed')
