
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    arr_len = len(nums)
    base = [1 for _ in range(arr_len)]

    prefix = 1
    for item in range(arr_len):
        base[item] = prefix
        prefix *= nums[item]

    postfix = 1
    for item in range(arr_len - 1, -1, -1):
        """
        we do this to multiply with the numbers in array thats left 
        [1, 1, 2, 6] by the moment after counting the prefix
        we starting to multiply in reverse order --> 1 * 1 --> 1 * 6
                                                     1 * 4 --> 4 * 2
                                                     4 * 3 --> 12 * 1
                                                     12 * 2 --> 24 * 1
        """
        base[item] *= postfix
        # postfix must be change by mult with 
        postfix *= nums[item]

    return base

if __name__ == "__main__":
    print(product_except_self(nums=[1, 2, 3, 4]))
