# Time: O(n), Space: O(n).
def is_balanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


if __name__ == '__main__':
    assert is_balanced('(a[b]{c})')
    assert not is_balanced('([)]')
    assert is_balanced('')
    assert is_balanced('hello')
    assert not is_balanced(')')
    assert not is_balanced('((')
    print('Challenge 1: all tests passed')
