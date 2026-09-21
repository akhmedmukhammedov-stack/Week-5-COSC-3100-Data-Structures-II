# Time: O(log n), Space: O(1). Input must be sorted in ascending order.
def search_range(nums: list[int], target: int) -> tuple[int, int]:
    def boundary(after_equal):
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target or (after_equal and nums[middle] == target):
                left = middle + 1
            else:
                right = middle
        return left

    first = boundary(False)
    if first == len(nums) or nums[first] != target:
        return -1, -1
    return first, boundary(True) - 1


if __name__ == '__main__':
    assert search_range([5, 7, 7, 8, 8, 8, 10], 8) == (3, 5)
    assert search_range([], 8) == (-1, -1)
    assert search_range([1, 3, 5], 4) == (-1, -1)
    assert search_range([2], 2) == (0, 0)
    assert search_range([2, 2, 2], 2) == (0, 2)
    assert search_range([1, 2, 3], 1) == (0, 0)
    assert search_range([1, 2, 3], 3) == (2, 2)
    print('Challenge 9: all tests passed')
