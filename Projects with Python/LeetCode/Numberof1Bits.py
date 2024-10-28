class Solution:
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        
        return res
    


print(bin(13))    
print(Solution().hammingWeight(13))