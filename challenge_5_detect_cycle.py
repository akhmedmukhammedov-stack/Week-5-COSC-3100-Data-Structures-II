from __future__ import annotations


class Node:
    def __init__(self, val, next: Node | None = None):
        self.val = val
        self.next = next


# Time: O(n), Space: O(1).
def has_cycle(head: Node | None) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == '__main__':
    assert not has_cycle(None)
    single = Node(1)
    assert not has_cycle(single)
    single.next = single
    assert has_cycle(single)
    a, b, c = Node(1), Node(1), Node(1)
    a.next, b.next = b, c
    assert not has_cycle(a)  # Equal values do not mean equal nodes.
    c.next = b
    assert has_cycle(a)
    print('Challenge 5: all tests passed')
