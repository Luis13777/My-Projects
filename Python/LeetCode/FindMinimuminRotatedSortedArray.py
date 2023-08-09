from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0

        r = len(nums) - 1

        if (nums[r] > nums[l] or r == l):
            return nums[l]
        while (True):
            m = int((l+r)/2)

            if (nums[m] > nums[m+1]):
                return nums[m+1]
            else:
                if nums[m] < nums[l]:
                    r = m
                else:
                    l = m

# O(log(n))
# O(1)
    

solution = Solution()

print(solution.findMin([2]))