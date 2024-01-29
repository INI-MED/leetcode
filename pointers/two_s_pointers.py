
from typing import List

def two_sum_pointers(nums: List[int], target: int) -> List[int]:
    
    left, right = 0, len(nums) - 1

    while left < right:

        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [nums[left], nums[right]]



def repeat1(nums: List[int], target: int) -> List[int]:

    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            return [nums[l], nums[r]]