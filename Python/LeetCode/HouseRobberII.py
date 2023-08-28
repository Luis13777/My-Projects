class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        best = {}

        def BreakInto(numberOfTheHouse):
            
            nonlocal best

            if numberOfTheHouse == len(nums) - 1:
                return nums[numberOfTheHouse]
            
            if numberOfTheHouse == len(nums) - 2:
                return nums[numberOfTheHouse]


            if (numberOfTheHouse in best):
                return best[numberOfTheHouse]
            
            money = nums[numberOfTheHouse]
            if numberOfTheHouse + 3 < len(nums):            
                money += max(BreakInto(numberOfTheHouse + 2), BreakInto(numberOfTheHouse + 3))
            else:
                money += BreakInto(numberOfTheHouse + 2)
            best[numberOfTheHouse] = money

            return money
        
        last = nums[-1]
        del(nums[-1])

        n1 = max(BreakInto(0), BreakInto(1))


        nums.append(last)

        del(nums[0])

        best = {}

        n2 = max(BreakInto(0), BreakInto(1))

        return max(n1, n2)
            
        


    