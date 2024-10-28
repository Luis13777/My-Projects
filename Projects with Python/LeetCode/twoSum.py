from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tamanho = len(nums)

        for k in range (tamanho - 1):
            for i in range (tamanho-k - 1):
                if (nums[k]+nums[tamanho-1-i] == target):
                    return [k, tamanho-1-i]
solution = Solution()

# print (solution.twoSum([2, 7, 11, 15], 9))


# Test case 1
nums = [2, 7, 11, 15]
target = 9
expected_output = [0, 1]
assert solution.twoSum(nums, target) == expected_output

# Test case 2
nums = [3, 2, 4]
target = 6
expected_output = [1, 2]
assert solution.twoSum(nums, target) == expected_output

# Test case 3
nums = [3, 3]
target = 6
expected_output = [0, 1]
assert solution.twoSum(nums, target) == expected_output

# Test case 4
nums = [-1, -2, -3, -4, -5]
target = -8
expected_output = [2, 4]
assert solution.twoSum(nums, target) == expected_output