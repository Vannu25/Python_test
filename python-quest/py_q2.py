"""Given an array of integers, write a function to find the maximum sum of any contiguous subarray
(i.e., the largest sum of consecutive elements) within the array.
E.g. for array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Answer is 6 -> subarray [4, -1, 2, 1]"""


def max_subarray_sum(nums):
    curr_max = nums[0] #-2
    glob_max = nums [0] # -2

    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i]) #
        glob_max = max(glob_max, curr_max)

    return glob_max

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_subarray_sum(nums)
print("The largest sum of consecutive elements", output)

