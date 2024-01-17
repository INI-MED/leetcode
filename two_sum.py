from typing import List, Dict


def counter(nums: List[int]) -> Dict[int, int]:
    hash_map = {}
    for ind, item in enumerate(nums):
        hash_map[item] = ind
    return hash_map


def two_sum(nums: List[int], target: int) -> List[int]:
    
    hash_map = counter(nums=nums)

    for item in nums:
        diff = target - item
        if diff in hash_map:
            return [hash_map[diff], hash_map[item]]


def two_sum_pointers(nums: List[int], target: int) -> List[int]:

    left, right = 0, len(nums) - 1

    while left < right:
        p_sum = nums[left] + nums[right]
        if p_sum > target:
            right -= 1
        elif p_sum < target:
            left += 1
        else:
            return [nums[left] + 1, nums[right] + 1]  # INFO: + 1 is only for leetcode


def _counter(nums: List[int]) -> Dict[int, int]:

    hash_map = {}
    for ind, item in enumerate(nums):
        hash_map[item] = ind
    return hash_map 

def two_sum_repeat(nums: List[int], target: int) -> List[int]:
    hash_map = counter(nums=nums)

    for item in nums:
        diff = taget - item

        if diff in hash_map:
            return [hash_map[diff], item]


if __name__ == "__main__":
    print(two_sum(nums=[2, 7, 11, 15], target=13))
