class Solution:
    def countBits(self, n):
        ans = []
        for i in range (n+1):
            count = 0
            while i:
                count += i & 1
                i = i >> 1
            ans.append(count)

        return ans
    
print(Solution().countBits(5))