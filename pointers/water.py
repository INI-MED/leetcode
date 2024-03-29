from typing import List


def most_water(height: List[int]) -> int:

    left, right = 0, len(height) - 1
    res = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        # ERROR: we move pointers to the right side if height on the left side is bigger than the height on the right side
        if height[left] < height[right]:
            right -= 1
        else:
            left += 1

        res = max(area, res)

    return res


def right_most_water(height: List[int]) -> int:

    left, right = 0, len(height) - 1
    res_area = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

        res_area = max(area, res_area)
    return res_area


def repeat1(height: List[int]) -> int:

    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        # NOTE: remember how to count square
        area = (l + r) * min(height[l], height[r])

        # ERROR: we subtract from the left pointer if height from left is bigger than right pointer
        if height[l] > height[r]:
            l += 1
        else:
            r -= 1

        res = max(area, res)
    return res
