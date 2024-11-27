class Solution:
    def search(self, nums, target):
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        
        # not sorted
        middle = 0
        if nums[-1] < nums[0]:
            # do binary search to find where is the lowest number
            l = 0
            r = len(nums) - 1
            middle = (r+l)//2
            while (nums[middle] > nums[middle - 1]):
                if nums[r] < nums[middle]:
                    l = middle + 1
                else:
                    r = middle - 1
                middle = (r+l)//2
                
            nums = nums[middle::] + nums[:middle:]

        # middle is the number of times it was rotated
        # do binary search

        l = 0
        r = len(nums) - 1
        m = (r+l)//2
        while (nums[m] != target and l < r):
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (r+l)//2
        if l >= r and nums[m] != target:
            return - 1
        
        return (m + middle)%(len(nums))
    
solution = Solution()

print(solution.search([1,3], 1))
        