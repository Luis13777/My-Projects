from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range (len(nums)):
            ans.append(nums[i])

        for i in range (len(nums)):
            ans.append(nums[i])

        return nums + nums
    
solution = Solution()

print(solution.getConcatenation([1,11,2,3]))