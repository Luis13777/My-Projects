class Solution:
    def fourSum(self, nums, target):

        if len(nums) < 4:
            return []
        
        ans = []
        nums = sorted(nums)
        i1 = 0
        i2 = 1
        i3 = 2
        i4 = 3

        while True:
            sum_of_nums = nums[i1] + nums[i2] + nums[i3] + nums[i4]
            if sum_of_nums < target:
                if i4 + 1 < len(nums):
                    i4 += 1
                else:
                    if i3 + 2 < len(nums):
                        i3 += 1
                        i4 = i3 + 1
                    else:
                        if i2 + 3 < len(nums):
                            i2 += 1
                            i3 = i2 + 1
                            i4 = i3 + 1
                        else:
                            if i1 + 4 < len(nums):
                                i1 += 1
                                i2 = i1 + 1
                                i3 = i2 + 1
                                i4 = i3 + 1
                            else:
                                return ans
            elif sum_of_nums > target:
                if i3 + 2 < len(nums):
                    i3 += 1
                    i4 = i3 + 1
                else:
                    if i2 + 3 < len(nums):
                        i2 += 1
                        i3 = i2 + 1
                        i4 = i3 + 1
                    else:
                        if i1 + 4 < len(nums):
                            i1 += 1
                            i2 = i1 + 1
                            i3 = i2 + 1
                            i4 = i3 + 1
                        else:
                            return ans
            else:
                array = [nums[i1], nums[i2], nums[i3], nums[i4]]
                if array not in ans:
                    ans.append(array)
                    if i4 + 1 < len(nums):
                        i4 += 1
                    else:
                        if i3 + 2 < len(nums):
                            i3 += 1
                            i4 = i3 + 1
                        else:
                            if i2 + 3 < len(nums):
                                i2 += 1
                                i3 = i2 + 1
                                i4 = i3 + 1
                            else:
                                if i1 + 4 < len(nums):
                                    i1 += 1
                                    i2 = i1 + 1
                                    i3 = i2 + 1
                                    i4 = i3 + 1
                                else:
                                    return ans
                else:
                    if i3 + 2 < len(nums):
                        i3 += 1
                        i4 = i3 + 1
                    else:
                        if i2 + 3 < len(nums):
                            i2 += 1
                            i3 = i2 + 1
                            i4 = i3 + 1
                        else:
                            if i1 + 4 < len(nums):
                                i1 += 1
                                i2 = i1 + 1
                                i3 = i2 + 1
                                i4 = i3 + 1
                            else:
                                return ans
        
solucao = Solution()
print(solucao.fourSum([1, 0, -1, 0, -2, 2], 0)) # [[-2,-1,0,1],[-2,0,0,2],[-1,0,0,1]]
print(solucao.fourSum([2, 2, 2, 2, 2], 8)) # [[2,2,2,2]]