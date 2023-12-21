
from typing import List


def duplicates(nums: List[int]) -> bool:

    hash_map = set()

    for item in nums:
        if item in hash_map:
            return True
        hash_map.add(item)
    return False


if __name__ == "__main__":
    print(duplicates(nums=[1, 2, 3, 4]))
