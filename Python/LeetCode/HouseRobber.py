class Solution:
    def rob(self, nums):

        if (len(nums) == 1):
            return nums[0]

        memory = {}

        def NextHouse (n):
            nonlocal memory

            if (n in memory):
                return memory[n]
            if (n >= len(nums)):
                return 0
            if (n == len(nums) - 1 or n == len(nums) - 2):
                memory[n] = nums[n]
                return nums[n]
            
            preco1 = nums[n]
            preco2 = nums[n]

            preco1 += NextHouse(n+2)
            preco2 += NextHouse(n+3)

            memory[n] = max (preco1, preco2)

            return max (preco1, preco2)
        


        return max(NextHouse(0), NextHouse(1))
    

solution = Solution()
print(solution.rob([1,2,3,112,3,4,5,8]))