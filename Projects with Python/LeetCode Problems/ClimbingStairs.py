class Solution:
    def climbStairs(self, n):

        numberOfWays = 0

        def Try (totalSteps):
            nonlocal numberOfWays
            if totalSteps == n:
                numberOfWays += 1
            elif totalSteps < n:
                if (totalSteps + 2 <= n):
                    Try (totalSteps + 2)
                Try (totalSteps + 1)

        Try(0)

        return numberOfWays
    







class Solution:
    def climbStairs(self, n):
        
        memory = {}

        def upStep (height):
            nonlocal memory

            if height in memory:
                return memory[height]
            if height == n:
                return 1
            elif height < n:
                
                possibilities = 0

                if (height + 2 <= n):
                    possibilities += upStep (height + 2)
                possibilities += upStep (height + 1)
            memory[height] = possibilities
            return possibilities
        
        return upStep (0)
    





solution = Solution ()

print(solution.climbStairs(38))

