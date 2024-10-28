class Solution:
    def removeDuplicates(self, nums):
        cur = nums[0]
        size = len(nums)
        i = 0
        numberOfDifferentNumbers = 0
        while (i < size):
            nums[numberOfDifferentNumbers] = cur
            while (i < size and nums[i] == cur):
                i += 1
            if (i < size):
                cur = nums[i]
                numberOfDifferentNumbers += 1
        numberOfDifferentNumbers += 1
        return numberOfDifferentNumbers
    
solution = Solution()
numbers = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(numbers))
print(numbers)