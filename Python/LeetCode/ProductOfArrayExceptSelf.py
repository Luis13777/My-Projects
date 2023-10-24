class Solution:
    def productExceptSelf(self, nums):
        ProductOfAll = 1
        numberOfZeros = 0
        i = 0
        positionOfTheOnlyZero = 0
        for num in nums:
            if num == 0:
                numberOfZeros += 1
                positionOfTheOnlyZero = i
            else:
                ProductOfAll = ProductOfAll*num
            i += 1

        if numberOfZeros >= 2:
            return [0 for i in range(len(nums))]
        elif numberOfZeros == 1:
            newArray = [0 for i in range(len(nums))]
            newArray[positionOfTheOnlyZero] = ProductOfAll
            return newArray
        newArray = []
        for num in nums:
            newArray.append(int(ProductOfAll/num))

        return newArray
    
solution = Solution().productExceptSelf

print(solution([-1,1,0,0,3]))