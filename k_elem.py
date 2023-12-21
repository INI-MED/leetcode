
from typing import List
from collections import defaultdict


def right_k(nums: List[int], k: int) -> List[int]:
    hash_map = {}

    freq = [[] for _ in range(len(nums) - 1)]

    for item in nums:
        hash_map[item] = 1 + hash_map.get(item, 0)

    for key, value in hash_map.items():
        freq[value].append(key)  # bucket sort algorithm

    res = []
    for item in range(len(freq) - 1, 0, -1):
        for n in freq[item]:
            res.append(n)
            if len(res) == k:
                return res


def k_freq_elem(nums: List[int], target: int) -> List[int]:

    hash_map = defaultdict(int)

    freq = [[] for _ in range(len(nums) + 1)]

    for item in nums:
        hash_map[item] = 1 + hash_map.get(item, 0) 

    for value in hash_map.values():
        for item in freq:
            item.append(value)
            if len(item) == target:
                return item




if __name__ == "__main__":
    right_k([1, 1, 1, 2, 2, 3], 2)



