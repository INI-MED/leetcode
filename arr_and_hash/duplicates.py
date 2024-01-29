
from typing import List


def duplicates(nums: List[int]) -> bool:

    hash_map = set()

    for item in nums:
        if item in hash_map:
            return True
        hash_map.add(item)
    return False


def dupl_repeat(nums: List[int]) -> bool:

    hash_set = set()
    for item in nums:
        if item in hash_set:
            return True
        hash_set.add(item)
    return False

if __name__ == "__main__":
    print(duplicates(nums=[1, 2, 3, 4]))
