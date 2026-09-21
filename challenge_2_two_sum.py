# Time: O(n) average, Space: O(n).
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        # Look up first so the same element cannot be used twice.
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    raise ValueError('No valid pair')


if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)
    assert two_sum([0, 4, 3, 0], 0) == (0, 3)
    assert two_sum([3, 3], 6) == (0, 1)
    print('Challenge 2: all tests passed')
