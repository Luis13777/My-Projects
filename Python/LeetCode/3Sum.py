class Solution:
    def threeSum(self, nums):
        
        nums = sorted(nums)
        answer = []

        for i in range (len(nums) - 2):
            l = i +1
            r = len(nums) - 1
            while (l<r):
                if nums[l] + nums[r] + nums[i] == 0:
                    if [nums[i], nums[l], nums[r]] not in answer:
                        answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        
        return answer
    
solution = Solution ()
print(solution.threeSum([0,0,0,0]))