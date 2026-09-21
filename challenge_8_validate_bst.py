from __future__ import annotations


class Node:
    def __init__(self, val, left: Node | None = None, right: Node | None = None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n), Space: O(h). Strict BST ordering rejects duplicate values.
def is_valid_bst(root: Node | None) -> bool:
    def check(node, low, high):
        if node is None:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    return check(root, None, None)


if __name__ == '__main__':
    assert is_valid_bst(None)
    assert is_valid_bst(Node(5))
    assert is_valid_bst(Node(5, Node(1), Node(8, Node(6), Node(9))))
    assert not is_valid_bst(Node(5, Node(1), Node(8, Node(4), Node(9))))
    assert not is_valid_bst(Node(5, Node(5)))
    assert is_valid_bst(Node(0, Node(-10), Node(10)))
    print('Challenge 8: all tests passed')
