from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:

    res = []
    nums.sort()
    for item in nums:
        if item == nums[item] + 1:
            continue

        left_p = 0
        right_p = len(nums) - 1

        while left_p < right_p:
            p_sum = nums[left_p] + nums[right_p] + item
            if p_sum > 0:
                right_p -= 1
            elif p_sum < 0:
                left_p += 1
            else:
                res.append([nums[left_p], nums[right_p], item])
                left_p += 1
                while nums[left_p] == nums[left_p - 1]:
                    left_p += 1

    return res

