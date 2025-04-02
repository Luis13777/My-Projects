class Solution:
    def threeSumClosest(self, nums, target):
        nums_sorted = sorted(nums)

        l = 0
        m = 1
        r = len(nums) - 1
        closest_distance = abs(nums_sorted[l] + nums_sorted[m] + nums_sorted[r] - target)
        ans = nums_sorted[l] + nums_sorted[m] + nums_sorted[r]

        while True:
            current_ans = nums_sorted[l] + nums_sorted[m] + nums_sorted[r] - target
            abs_current_ans = abs(current_ans)
            if abs_current_ans < closest_distance:
                closest_distance = abs_current_ans
                ans = nums_sorted[l] + nums_sorted[m] + nums_sorted[r]
            if current_ans < 0:
                m += 1
            elif current_ans > 0:
                r -= 1
            else:
                return target

            if m == r:
                r = len(nums) - 1
                l += 1
                m = l + 1
                if m == r:
                    return ans
            
            
    
questao = Solution()
print(questao.threeSumClosest([0, 0, 0], 1))  # Output: 2
            
            
