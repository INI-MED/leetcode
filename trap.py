

def trapping_water(height: List[int]) -> int:

    l, r = 0, len(height) - 1
    max_l = height[l]
    max_r = height[r]
    res = 0
    while l < r:

        if max_l < max_r:
            l += 1
            max_l = max(height[l], max_l)
            # ERROR: otherwise --> max_l - height[l]
            res += height[l] - max_l
        else:
            r -= 1
            max_r = max(height[r], max_r)
            # ERROR: otherwise --> max_r - height[r]
            res += height[r] - max_r

    return res

