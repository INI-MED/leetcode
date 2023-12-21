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


def three_sum1(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for ind, val in enumerate(nums):
        if ind > 0 and nums[ind] == nums[ind - 1]:
            continue

        l, r = ind + 1, len(nums) - 1

        while l < r:
           three_sum = val + nums[l] + nums[r]

           if three_sum < 0:
               l += 1
           elif three_sum > 0:
               r -= 1
           else:
               res.append([val, nums[l], nums[r]])
               l += 1
               # [-2, -2, 0, 0, 2, 2] 
               while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
