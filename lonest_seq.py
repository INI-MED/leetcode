from typing import List


def right_sequence(nums: List[int]) -> int:
    nums_set = set(nums)

    seq = 0 

    for item in nums:
        if (item - 1) not in nums_set:  # doesnt have left neighbour
            length = 0 
            while (item + length) in nums_set:  # check right neighbour
                length += 1 

            seq = max(seq, length)

    return seq


def longest_sequence(nums: List[int]) -> int:

    nums_set = set(nums)

    freq = 0

    for item in nums_set:
        if item - 1 in nums_set:
            length = 0

            while item + 1 in nums_set:
                length += 1

            freq = max(freq, length)

    return freq

if __name__ == "__main__":
    print(right_sequence([100, 4, 200, 1, 3, 2]))
