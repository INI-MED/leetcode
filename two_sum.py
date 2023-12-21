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


if __name__ == "__main__":
    print(two_sum(nums=[2, 7, 11, 15], target=13))
